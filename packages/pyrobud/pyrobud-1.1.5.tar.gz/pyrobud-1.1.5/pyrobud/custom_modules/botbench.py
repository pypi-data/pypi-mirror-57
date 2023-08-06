import asyncio
import statistics

from scipy.stats.mstats import gmean

from .. import command, module, util


class BotBenchModule(module.Module):
    name = "Bot Bench"

    @command.desc("Bot benchmark")
    async def cmd_bench(self, msg, n):
        chat = await msg.get_chat()
        deltas = []

        async with self.bot.client.conversation(chat) as conv:
            for _ in range(10):
                await conv.send_message("/start")
                before = util.time.usec()
                await conv.get_response()
                after = util.time.usec()
                deltas.append(after - before)

        return f"""**{n}**
Mean: **{util.time.format_duration_us(statistics.mean(deltas))}**
Geometric mean: {util.time.format_duration_us(gmean(deltas))}
Median: {util.time.format_duration_us(statistics.median(deltas))}"""
