import genshinstats as gs
import json as js

def autoCheckIn():
    """
    attempt to auto check in upon starting program,
    """
    try:
        if reward := gs.claim_daily_reward() is not None:
            print(f"Claimed daily reward - {reward['cnt']}x {reward['name']}")
        else:
            print("Could not claim daily reward")
    except Exception as e:
        print(e)


def tmp():
    import schedule
    import time
    schedule.every().day.at('00:00').do(autoCheckIn)
    while True:
        schedule.run_pending()
        time.sleep(1)


def configCookie():
    t = gs.get_browser_cookies()
    if not t:  # failed to get cookies
        # read cookies from config file
        ltuid, ltoken = input("ltuid: "), input("ltoken: ")
        t = {'ltuid':ltuid, 'ltoken':ltoken}
    gs.set_cookie(t)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    configCookie()
    autoCheckIn()
    tmp()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
