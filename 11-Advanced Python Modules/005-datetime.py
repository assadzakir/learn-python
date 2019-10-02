# Date time
print('=============================================')

import datetime

print('=================Time============================')

t = datetime.time()

print(t)  # 00:00:00

t = datetime.time(2, 25, 2)

print(t)  # 02:25:02

print(datetime.time)  # <class 'datetime.time'>

print(datetime.time.min)  # 00:00:00

print(datetime.time.max)  # 23:59:59.999999

print(datetime.time.resolution)  # 0:00:00.000001

print('=================Date============================')


print(datetime.date.today())  # current date Format"2017-11-11"

print(datetime.date.today().timetuple())
                                        # time.struct_time(
                                        # tm_year=2017,
                                        # tm_mon=11,
                                        # tm_mday=11,
                                        # tm_hour=0,
                                        # tm_min=0,
                                        # tm_sec=0,
                                        # tm_wday=5,
                                        # tm_yday=315,
                                        # tm_isdst=-1)

print(datetime.date.today().day)  # 11

print(datetime.date.min)  # 0001-01-01

print(datetime.date.max)  # 9999-12-31

print(datetime.date.resolution)  # 1 day, 0:00:00

date1 = datetime.date(2017,11,11)

date2 = date1.replace(2018,11,11)

print(date1) # 2017-11-11

print(date2) # 2018-11-11

print(date1 - date2) # -365 days, 0:00:00
