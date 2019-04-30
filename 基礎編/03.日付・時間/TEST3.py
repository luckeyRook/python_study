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


#日付計算
todaydatil = datetime.datetime.today()

#今日の日付
print(todaydatil)

#明日の日付
print(todaydatil + datetime.timedelta(days=1))

newyear = datetime.datetime(2010,1,1)

#2010年の一週間後
print(newyear + datetime.timedelta(days=7))


#2010年から今日までの日数
#なお、dateとdatetimeでちゃんと計算しないとerrorが発生
calc = todaydatil - newyear

#計算結果の戻り値はtimedetila型
print(calc.days)

#うるう年判定
import calendar

print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))

print(calendar.leapdays(2010,2020))