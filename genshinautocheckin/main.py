import genshinstats as gs
import sys


def autoCheckIn() -> None:
    """
    attempt to auto check in upon starting program,
    """
    try:
        reward = gs.claim_daily_reward()
        if reward is not None:
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

    cookies = {}

    if len(args) != 3:
        print('Usage: main.exe <ltuid> <ltoken>')
        cookies = gs.get_browser_cookies()
    else:
        cookies = {'ltuid': args[1], 'ltoken': args[2]}

    gs.set_cookies(cookies)


def main():
    configCookie()
    autoCheckIn()
    tmp()


if __name__ == '__main__':
    main()
