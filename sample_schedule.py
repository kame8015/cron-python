import schedule
import time
from datetime import datetime, timezone, timedelta
import sys


class PrintNow:
    def __init__(self):
        self.count = 0

    def print_now(self):
        """現在時刻をUNIX時刻で取得し変換して表示する"""
        JST = timezone(timedelta(hours=+9), "JST")
        now_unix = int(time.time())
        now = datetime.fromtimestamp(now_unix, JST)
        self.count += 1
        print("------")
        print(f"Count: {self.count}")
        print(f"Now: {now}")


def __validate_args(args) -> int:
    """コマンドライン引数の検証"""
    if args is None:
        raise Exception("args must be set.")

    try:
        pending_time = int(args)
    except Exception:
        raise Exception("args must be int.")

    if not pending_time > 0:
        raise Exception("args must be greater than 0.")

    return pending_time


if __name__ == "__main__":
    args = sys.argv
    pending_time = __validate_args(args[1])

    pn = PrintNow()
    # 入力された秒ごとに print_now 関数を呼び出す
    schedule.every(pending_time).seconds.do(pn.print_now)

    while True:
        schedule.run_pending()
