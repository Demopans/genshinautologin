import genshinstats as gs
import sys


def autoCheckIn() -> None:
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


def tmp() -> None:
    import schedule
    import time
    schedule.every().day.at('00:00').do(autoCheckIn)
    while True:
        schedule.run_pending()
        time.sleep(1)


def configCookie() -> None:
    args: list[str] = sys.argv
    if len(args) != 3:
        print('autosign.c <ltuid> <ltoken>')
        sys.exit(2)

    t = gs.get_browser_cookies()
    if not t:  # failed to get cookies
        # read cookies from config file
        t = {'ltuid': args[1], 'ltoken': args[2]}
    gs.set_cookie(t)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    configCookie()
    autoCheckIn()
    tmp()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
