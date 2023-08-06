import asyncio

import telethon as tg


TRUNCATION_SUFFIX = "... (truncated)"


def mention_user(user):
    if user.username:
        # Use username mention if possible
        name = f"@{user.username}"
    else:
        # Use the first and last name otherwise
        name = tg.utils.get_display_name(user)
        if not name:
            # Deleted accounts have no name; behave like the official clients
            name = "Deleted Account"

    return f"[{name}](tg://user?id={user.id})"


def filter_code_block(inp):
    if inp.startswith("```") and inp.endswith("```"):
        inp = inp[3:][:-3]
    elif inp.startswith("`") and inp.endswith("`"):
        inp = inp[1:][:-1]

    return inp


async def msg_download_file(ctx, download_msg, destination=bytes, file_type="file"):
    last_percent = -5

    def prog_func(current_bytes, total_bytes):
        nonlocal last_percent

        if not ctx:
            return

        # Only edit message if progress >= 5% to mitigate API flooding
        percent = int((current_bytes / total_bytes) * 100)
        if abs(percent - last_percent) >= 5:
            loop = asyncio.get_event_loop()
            loop.create_task(ctx.respond(f"Downloading {file_type}... {percent}% complete"))

        last_percent = percent

    return await download_msg.download_media(file=destination, progress_callback=prog_func)


def truncate(text):
    if len(text) > 4096:
        return text[: 4096 - len(TRUNCATION_SUFFIX)] + TRUNCATION_SUFFIX
    else:
        return text
