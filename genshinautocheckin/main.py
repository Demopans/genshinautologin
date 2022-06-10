import asyncio
import sys

import genshin.client
import genshin.utility

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
            from platform import system
            if system() == 'Windows':
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            reward = asyncio.run(c.claim_daily_reward())
        except genshin.AlreadyClaimed as e:
            txt = "Already claimed the daily reward today.\n"
        except RuntimeError as e:
            txt = f"RuntimeError: {e}\n"
        except Exception as e:
            txt = f"{e}\n"
        else:
            txt = f"Claimed {reward.amount}x\"{reward.name}\n"
        print(txt)
        log.write(txt)
        log.flush()


    def servideMgr():
        import schedule, time
        def service():
            import threading as tp
            pool = [tp.Thread(target=task, args=(i,)) for i in usr]
            for i in pool:
                i.start()
            for i in pool:
                i.join()

        service()
        schedule.every().day.at('00:00').do(service)
        while True:
            schedule.run_pending()
            time.sleep(1)

    usr: list[genshin.client.Client] = []
    log = open("./log.txt", 'w+')
    configCookie(len(sys.argv) > 1)
    print('\n\n\n\n')
    sys.stdout.flush()
    servideMgr()
