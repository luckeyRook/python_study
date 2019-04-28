#日付と時間
import datetime

today=datetime.date.today()
todaydatil=datetime.datetime.today()

#今日の日付
print('----------------------')
print(today)
print(todaydatil)

#今日の日付：それぞれの値
print('----------------------')
print(today.year)
print(today.month)
print(today.day)
print(todaydatil.year)
print(todaydatil.month)
print(todaydatil.day)
print(todaydatil.hour)
print(todaydatil.minute)
print(todaydatil.second)
print(todaydatil.microsecond)

#日付のフォーマット
print('----------------------')
print(today.isoformat())
print(todaydatil.strftime("%Y/%m/%d %H:%M:%S"))
