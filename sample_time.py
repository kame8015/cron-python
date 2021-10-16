import time
import sys
from datetime import datetime, timezone, timedelta


class PrintNow:
    def __init__(self):
        self.count = 0
        self.JST = timezone(timedelta(hours=+9), "JST")

    def print_now(self):
        """現在時刻をUNIX時刻で取得し変換して表示する"""
        now_unix = int(time.time())
        now = datetime.fromtimestamp(now_unix, self.JST)
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

    if pending_time <= 0 or 60 < pending_time:
        raise Exception("args must be greater than 0 and less than 60.")

    return pending_time


if __name__ == "__main__":
    args = sys.argv
    pending_time = __validate_args(args[1])

    pn = PrintNow()

    while True:
        now_unix = int(time.time())
        now = datetime.fromtimestamp(now_unix, pn.JST)
        # 入力された秒ごとに print_now 関数を呼び出す
        if now.second % pending_time == 0:
            pn.print_now()
        time.sleep(1)  # 1秒待つ
