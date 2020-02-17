from datetime import datetime, timedelta
import datetime

HoraCredito = '10:11:00'
h, m, s = (map(int, HoraCredito.split(':')))
HoraCredito = datetime.timedelta(0,s,0,0,m,h)

HoraDebito = '08:41:00'
h, m, s = (map(int, HoraDebito.split(':')))
HoraDebito = datetime.timedelta(0,s,0,0,m,h)

print(HoraCredito - HoraDebito);
