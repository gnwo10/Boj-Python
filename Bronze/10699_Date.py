import sys

input = sys.stdin.readline

from datetime import datetime

now_kst = datetime.now()
today_kst = now_kst.date()    # 오늘 날짜 (KST)

print(today_kst)