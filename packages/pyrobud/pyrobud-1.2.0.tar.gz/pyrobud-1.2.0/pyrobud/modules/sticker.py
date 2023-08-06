import asyncio
import io
import os
import subprocess
import time
from datetime import datetime

from PIL import Image

from .. import command, module, util

PNG_MAGIC = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"

# Sticker bot's error strings
TOO_MANY_STICKERS_ERROR = "A pack can't have more than 120 stickers at the moment."
INVALID_FORMAT_ERROR = "Sorry, the file type is invalid."
IMAGE_TOO_BIG_ERROR = "Sorry, the file is too big."


class LengthMismatchError(Exception):
    pass


class StickerModule(module.Module):
    name = "Sticker"

    async def on_load(self):
        self.db = self.bot.get_db("stickers")
        self.settings_db = self.bot.get_db("sticker_settings")

    async def add_sticker(self, sticker_data, pack_name, emoji="❓"):
        # User to send messages to
        target = "Stickers"

        commands = [
            ("text", "/cancel"),
            ("text", "/addsticker"),
            ("text", pack_name),
            ("file", sticker_data),
            ("text", emoji),
            ("text", "/done"),
        ]

        success = False
        before = datetime.now()

        async with self.bot.client.conversation(target) as conv:

            async def reply_and_ack():
                # Wait for a response
                response = await conv.get_response()
                # Ack the response to suppress its notiication
                await conv.mark_read()

                return response

            try:
                for cmd_type, data in commands:
                    if cmd_type == "text":
                        await conv.send_message(data)
                    elif cmd_type == "file":
                        await conv.send_file(data, force_document=True)
                    else:
                        raise TypeError(f"Unknown command type '{cmd_type}'")

                    # Wait for both the rate-limit and the bot's response
                    try:
                        wait_task = self.bot.loop.create_task(reply_and_ack())
                        ratelimit_task = self.bot.loop.create_task(asyncio.sleep(0.25))
                        await asyncio.wait({wait_task, ratelimit_task})

                        response = wait_task.result()
                        if TOO_MANY_STICKERS_ERROR in response.raw_text:
                            return (
                                False,
                                f"Sticker creation failed because there are too many stickers in the [{pack_name}](https://t.me/addstickers/{pack_name}) pack — Telegram's limit is 120. Delete some unwanted stickers or create a new pack.",
                            )
                        elif INVALID_FORMAT_ERROR in response.raw_text:
                            return (
                                False,
                                "Sticker creation failed because Telegram rejected the uploaded image file for deviating from their expected format. This is usually indicative of a MIME type issue in this bot.",
                            )
                        elif IMAGE_TOO_BIG_ERROR in response.raw_text:
                            return (
                                False,
                                "Sticker creation failed because the original image converted into WEBP format was above Telegram's 512 KiB size limit.",
                            )
                    except asyncio.TimeoutError:
                        after = datetime.now()
                        delta_seconds = int((after - before).total_seconds())

                        return (
                            False,
                            f"Sticker creation failed after {delta_seconds} seconds because [the bot](https://t.me/{target}) failed to respond within 1 minute of issuing the last command.",
                        )

                success = True
            finally:
                # Cancel the operation if we return early
                if not success:
                    await conv.send_message("/cancel")

        return (True, f"https://t.me/addstickers/{pack_name}")

    async def img_to_png(self, src, dest=None):
        if not dest:
            dest = src

        def _img_to_png():
            im = Image.open(src).convert("RGBA")
            if hasattr(src, "seek"):
                src.seek(0)
            im.save(dest, "png")

        await util.run_sync(_img_to_png)
        return dest

    async def img_to_sticker(self, src, formats):
        if not formats:
            return

        def _img_to_sticker():
            im = Image.open(src).convert("RGBA")

            sz = im.size
            target = 512
            if sz[0] > sz[1]:
                w_ratio = target / float(sz[0])
                h_size = int(float(sz[1]) * float(w_ratio))
                im = im.resize((target, h_size), Image.LANCZOS)
            else:
                h_ratio = target / float(sz[1])
                w_size = int(float(sz[0]) * float(h_ratio))
                im = im.resize((w_size, target), Image.LANCZOS)

            for fmt, dest in formats.items():
                im.save(dest, fmt)

        await util.run_sync(_img_to_sticker)
        return formats

    @command.desc("Kang a sticker into configured/provided pack")
    @command.usage("[sticker pack short name?]", optional=True)
    async def cmd_kang(self, ctx: command.Context):
        pack_name = ctx.input

        if not ctx.msg.is_reply:
            return "__Reply to a sticker to kang it.__"

        saved_pack_name = await self.settings_db.get("kang_pack")
        if not saved_pack_name and not pack_name:
            return "__Specify the name of the pack to add the sticker to.__"

        if pack_name:
            await self.settings_db.put("kang_pack", pack_name)
        else:
            pack_name = saved_pack_name

        reply_msg = await ctx.msg.get_reply_message()

        if not reply_msg.sticker:
            return "__That message isn't a sticker.__"

        await ctx.respond("Kanging sticker...")

        sticker_bytes = await reply_msg.download_media(file=bytes)
        sticker_buf = io.BytesIO(sticker_bytes)
        await self.img_to_png(sticker_buf)

        sticker_buf.seek(0)
        sticker_buf.name = "sticker.png"
        status, result = await self.add_sticker(sticker_buf, pack_name, emoji=reply_msg.file.emoji)
        if status:
            self.bot.dispatch_event_nowait("stat_event", "stickers_created")
            return f"[Sticker kanged]({result})."
        else:
            return result

    @command.desc("Save a sticker with a name (as a reference)")
    @command.usage("[new sticker name]")
    async def cmd_save(self, ctx: command.Context):
        name = ctx.input

        if not ctx.msg.is_reply:
            return "__Reply to a sticker to save it.__"

        if await self.db.has(name):
            return "__There's already a sticker with that name.__"

        reply_msg = await ctx.msg.get_reply_message()

        if not reply_msg.sticker:
            return "__That message isn't a sticker.__"

        await self.db.put(name, reply_msg.file.id)
        return f"Sticker saved as `{name}`."

    @command.desc("Save a sticker with a name (to disk)")
    @command.usage("[new sticker name]")
    async def cmd_saved(self, ctx: command.Context):
        name = ctx.input

        if not ctx.msg.is_reply:
            return "__Reply to a sticker to save it.__"

        if await self.db.has(name):
            return "__There's already a sticker with that name.__"

        reply_msg = await ctx.msg.get_reply_message()

        if not reply_msg.sticker:
            return "__That message isn't a sticker.__"

        path = await util.tg.msg_download_file(ctx, reply_msg, destination=f"stickers/{name}.webp", file_type="sticker")
        if not path:
            return "__Error downloading sticker__"

        await self.db.put(name, path)
        return f"Sticker saved to disk as `{name}`."

    @command.desc("List saved stickers")
    async def cmd_stickers(self, ctx: command.Context):
        out = ["**Stickers saved**:"]

        async for key, value in self.db:
            typ = "local" if value.endswith(".webp") else "reference"
            out.append(f"{key} ({typ})")

        if len(out) == 1:
            return "__No stickers saved.__"

        return "\n    \u2022 ".join(out)

    @command.desc("List locally saved stickers")
    async def cmd_stickersp(self, ctx: command.Context):
        out = ["**Stickers saved**:"]

        async for key, value in self.db:
            if value.endswith(".webp"):
                out.append(key)

        if len(out) == 1:
            return "__No stickers saved.__"

        return "\n    \u2022 ".join(out)

    @command.desc("Delete a saved sticker")
    @command.usage("[sticker name]")
    async def cmd_sdel(self, ctx: command.Context):
        name = ctx.input

        if not await self.db.has(name):
            return "__That sticker doesn't exist.__"

        await self.db.delete(name)
        return f"Sticker `{name}` deleted."

    @command.desc("Fetch a sticker by name")
    @command.usage("[sticker name]")
    async def cmd_s(self, ctx: command.Context):
        name = ctx.input

        path = await self.db.get(name)
        if path is None:
            return "__That sticker doesn't exist.__"

        await ctx.respond("Uploading sticker...")
        await ctx.respond(file=path, mode="repost")

    @command.desc("Fetch a sticker by name and send it as a photo")
    @command.usage("[sticker name]")
    @command.alias("sphoto")
    async def cmd_sp(self, ctx: command.Context):
        name = ctx.input

        webp_path = await self.db.get(name)
        if webp_path is None:
            return "__That sticker doesn't exist.__"

        if not webp_path.endswith(".webp"):
            return "__That sticker can't be sent as a photo.__"

        await ctx.respond("Uploading sticker...")
        png_path = webp_path[: -len(".webp")] + ".png"
        if not os.path.isfile(png_path):
            await self.img_to_png(webp_path, dest=png_path)

        await ctx.respond(file=png_path, mode="repost")

    @command.desc("Create a sticker from an image and add it to the given pack")
    @command.usage("[sticker pack name] [emoji to associate?]")
    async def cmd_sticker(self, ctx: command.Context):
        if not ctx.msg.is_reply and not ctx.msg.file:
            return "__Reply to or embed an image to sticker it.__"

        if ctx.msg.file:
            reply_msg = ctx.msg
        else:
            reply_msg = await ctx.msg.get_reply_message()

        if not reply_msg.file:
            return "__That message doesn't contain an image.__"

        pack_name = ctx.args[0]
        emoji = ctx.args[1] if len(ctx.args) > 1 else "❓"

        await ctx.respond("Creating sticker...")

        sticker_bytes = await reply_msg.download_media(file=bytes)
        sticker_buf = io.BytesIO(sticker_bytes)

        png_buf = io.BytesIO()
        webp_buf = io.BytesIO()
        await self.img_to_sticker(sticker_buf, {"png": png_buf, "webp": webp_buf})

        png_buf.seek(0)
        png_buf.name = "sticker.png"
        status, result = await self.add_sticker(png_buf, pack_name, emoji=emoji)
        if status:
            self.bot.dispatch_event_nowait("stat_event", "stickers_created")
            await ctx.respond(f"[Sticker created]({result}). Preview:")

            webp_buf.seek(0)
            webp_buf.name = "sticker.webp"
            await ctx.msg.respond(file=webp_buf)
        else:
            return result

    @command.desc("Create a sticker from an image and save it to disk under the given name")
    @command.usage("[new sticker name]")
    async def cmd_qstick(self, ctx: command.Context):
        name = ctx.input

        if not ctx.msg.is_reply and not ctx.msg.file:
            return "__Reply to an image to sticker it.__"

        if await self.db.has(name):
            return "__There's already a sticker with that name.__"

        if ctx.msg.file:
            reply_msg = ctx.msg
        else:
            reply_msg = await ctx.msg.get_reply_message()

        if not reply_msg.file:
            return "__That message isn't an image.__"

        await ctx.respond("Creating sticker...")

        sticker_bytes = await reply_msg.download_media(file=bytes)
        sticker_buf = io.BytesIO(sticker_bytes)

        path = f"stickers/{name}.webp"
        await self.img_to_sticker(sticker_buf, {"webp": path})

        self.db.put(name, path)
        self.bot.dispatch_event_nowait("stat_event", "stickers_created")
        return f"Sticker saved to disk as `{name}`."

    @command.desc("Glitch an image")
    @command.usage("[block offset strength?]", optional=True)
    async def cmd_glitch(self, ctx: command.Context):
        if not ctx.msg.is_reply and not ctx.msg.file:
            return "__Reply to an image to glitch it.__"

        boffset = 8
        if ctx.input:
            try:
                boffset = int(ctx.input)
            except ValueError:
                return "__Invalid distorted block offset strength.__"

        if ctx.msg.file:
            reply_msg = ctx.msg
        else:
            reply_msg = await ctx.msg.get_reply_message()

        if not reply_msg.file:
            return "__That message isn't an image.__"

        await ctx.respond("Glitching image...")

        orig_bytes = await reply_msg.download_media(file=bytes)

        # Convert to PNG if necessary
        if orig_bytes.startswith(PNG_MAGIC):
            png_bytes = orig_bytes
        else:
            png_buf = io.BytesIO(orig_bytes)
            await self.img_to_png(png_buf)
            png_bytes = png_buf.getvalue()

        # Invoke external 'corrupter' program to glitch the image
        # Source code: https://github.com/r00tman/corrupter
        command = ["corrupter", "-boffset", str(boffset), "-"]
        try:
            proc = await util.run_sync(
                lambda: subprocess.run(
                    command, input=png_bytes, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=15
                )
            )
        except subprocess.TimeoutExpired:
            return "🕑 `corrupter` failed to finish within 15 seconds."
        except subprocess.CalledProcessError as err:
            return f"⚠️ `corrupter` failed with return code {err.returncode}. Error: ```{err.stderr}```"
        except FileNotFoundError:
            return "❌ The `corrupter` [program](https://github.com/r00tman/corrupter) must be installed on the host system."

        glitched_bytes = proc.stdout
        await ctx.respond(file=glitched_bytes, mode="repost")
