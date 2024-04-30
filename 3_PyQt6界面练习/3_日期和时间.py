from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

# 获取日期，日期和时间，时间方法
now = QDate.currentDate()
print(now.toString(Qt.DateFormat.ISODate))
print(now.toString(Qt.DateFormat.RFC2822Date))

datatime = QDateTime.currentDateTime()
print(datatime.toString(Qt.DateFormat.ISODate))

time = QTime.currentTime()
print(time.toString(Qt.DateFormat.ISODate))

# 获取UTC时间
utc_now = QDateTime.currentDateTime()
print(f'本地时间{utc_now.toString(Qt.DateFormat.ISODate)}')
print(f'世界时间{utc_now.toUTC().toString(Qt.DateFormat.ISODate)}')
print(f'本地时间和世界时间差是{utc_now.offsetFromUtc()} seconds')

# 获取天数
d = QDate(2024, 5, 4)
print(f'指定月份的天数{d.daysInMonth()}')
print(f'指定年份的天数{d.daysInYear()}')

# 获取天数差
now_date = QDate.currentDate()
y = now_date.year()
print(f'今天的日期是{now_date.toString(Qt.DateFormat.ISODate)}')

xmas1 = QDate(y-1, 12, 25)
xmas2 = QDate(y, 12, 25)

dayspassed = xmas1.daysTo(now_date)
print(f'距上一个圣诞节已经过去{dayspassed}天')

nofdays = now_date.daysTo(xmas2)
print(f'下一个圣诞节还有{nofdays}天')

# 时间的计算
now_time = QDateTime.currentDateTime()
print(f'今天是：{now_time.toString(Qt.DateFormat.ISODate)}')
print(f'未来12天：{now_time.addDays(12).toString(Qt.DateFormat.ISODate)}')
print(f'过去22天是：{now_time.addDays(-22).toString(Qt.DateFormat.ISODate)}')

print(f'未来50秒是：{now_time.addSecs(50).toString(Qt.DateFormat.ISODate)}')
print(f'未来3个月是：{now_time.addMonths(3).toString(Qt.DateFormat.ISODate)}')
print(f'未来12年是：{now_time.addYears(12).toString(Qt.DateFormat.ISODate)}')
