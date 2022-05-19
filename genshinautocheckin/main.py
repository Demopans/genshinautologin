import asyncio
import datetime
from typing import TextIO, Mapping, BinaryIO, Any, Coroutine
from cryptography.fernet import Fernet
import os.path
import genshin.client
import genshin.utility
import asyncio
import sys


if __name__ == '__main__':
    # do on startup
    def configCookie(c: genshin.client.Client, log: TextIO, override=False) -> None:
        usr = []
        def writeData(strr: str) -> None:
            data: BinaryIO = open("./data", "ab+")

            key: bytes = Fernet.generate_key()
            with open("./key", "wb") as key_file:
                key_file.write(key)
                key_file.close()

            f = Fernet(key)
            enc = f.encrypt(strr.encode())
            data.write(enc+'\n'.encode())
            data.close()

        def readFromData():
            key = open("./key", "rb").read()
            data = open("./data", "rb+").read()
            f = Fernet(key)
            t = f.decrypt(data).decode().split("\n")
            for i in t:
                if i == '':
                    break
                tt = i.split()
                usr.append({"ltuid": tt[0], "ltoken": tt[1]})

        dataExists = os.path.exists("./data") and os.path.exists("./key")
        if override:
            #clear file
            data = open("./data", "wb+")
            data.close()

            writeData(open(sys.argv[1]).read())
            readFromData()
        else:
            if dataExists:
                readFromData()
            else:
                cookies: Mapping[str, str] = genshin.utility.get_browser_cookies()
                if len(cookies.keys()) == 0:
                    log.write(f"[{datetime.datetime.now()}]ERROR: Failed to get cookies")
                    exit(-1)
                writeData(f"{cookies['ltuid']} {cookies['ltoken']}\n")
        c.set_cookies(usr)

    async def task(c: genshin.client.Client, log):
        """
        attempt to auto check in upon starting program,
        """
        try:
            reward = await c.claim_daily_reward()
        except Exception:
            log.write("Daily reward already claimed")
        else:
            log.write(f"Claimed {reward.amount}x\"{reward.name}\"")
        log.flush()

    def service(c: genshin.client.Client, log):
        import schedule
        import time
        asyncio.run(task(c,log))
        schedule.every().day.at('00:00').do(task, c, log)
        while True:
            schedule.run_pending()
            time.sleep(1)

    cli = genshin.client.Client()

    log = open("./log.txt", 'w+')
    configCookie(cli, log, len(sys.argv) > 1)
    service(cli, log)
