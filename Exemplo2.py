import datetime

time1 = '8:00:00'
h, m, s = (map(int, time1.split(':')))
time10 = datetime.timedelta(0,s,0,0,m,h)

time2 = '8:30:00'
h, m, s = (map(int, time2.split(':')))
time20 = datetime.timedelta(0,s,0,0,m,h)

print(time20)

time20 - time10

#datetime.timedelta(0, 205)
print(time20 - time10)
