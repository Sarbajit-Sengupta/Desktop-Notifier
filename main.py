import argparse
import math
import time


def positive_interval(value):
    seconds = float(value)
    if not math.isfinite(seconds) or seconds <= 0:
        raise argparse.ArgumentTypeError("interval must be a finite positive number")
    return seconds


def run(interval, notify, sleep=time.sleep):
    try:
        while True:
            notify(title=' 💧  Drink Water!',
                   message='We have to drink water to stay hydrated!',
                   app_icon=None, timeout=10, toast=False)
            sleep(interval)
    except KeyboardInterrupt:
        return


def main():
    parser = argparse.ArgumentParser(description='Periodic desktop water reminder')
    parser.add_argument('--interval', type=positive_interval, default=10,
                        help='seconds between reminders (default: 10)')
    args = parser.parse_args()
    from plyer import notification
    run(args.interval, notification.notify)


if __name__ == '__main__':
    main()
