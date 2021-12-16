# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def autoCheckIn():
    """
    attempt to auto check in upon starting program,
    """
    import genshinstats as gs
    gs.set_cookie_auto()
    reward = gs.claim_daily_reward()
    if reward is not None:
        print(f"Claimed daily reward - {reward['cnt']}x {reward['name']}")
    else:
        print("Could not claim daily reward")


def tmp():
    import schedule
    import time
    schedule.every().day.at('17:00').do(autoCheckIn)
    while True:
        schedule.run_pending()
        time.sleep(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    autoCheckIn()
    tmp()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
