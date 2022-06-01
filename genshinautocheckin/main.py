import asyncio
import datetime
from typing import TextIO, Mapping, BinaryIO, Any, Coroutine
import genshin.client
import genshin.utility
import sys

if __name__ == '__main__':
    # do on startup
    def configCookie(override=False) -> None:
        if override:
            for ln in open(sys.argv[1]).read().split('\n'):
                t = ln.split(' ')
                usr.append(genshin.client.Client({'ltoken': t[0], 'ltuid': t[1]}, game=genshin.Game.GENSHIN))
        else:
            usr.append(genshin.client.Client(genshin.utility.get_browser_cookies(), game=genshin.Game.GENSHIN))


    def task(c: genshin.client.Client):
        """
        attempt to auto check in upon starting program,
        """
        try:
            reward = asyncio.run(c.claim_daily_reward())
        except Exception as e:
            txt = f"{e}\n"
        else:
            txt = f"Claimed {reward.amount}x\"{reward.name}\""
        print(txt)
        log.write(txt)
        log.flush()


    def servideMgr():
        import schedule
        def service():
            import multiprocessing as mp
            with mp.pool.ThreadPool(mp.cpu_count()) as pool:
                pool.map_async(task, usr)

        service()
        while True:
            schedule.every().day.at('00:00').do(service)


    usr: list[genshin.client.Client] = []
    log = open("./log.txt", 'w+')
    configCookie(len(sys.argv) > 1)
    servideMgr()
