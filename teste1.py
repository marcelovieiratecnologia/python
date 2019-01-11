from datetime import datetime, timedelta
import time
import datetime
import operator

#definindo o formato da hora
date_format = "%H:%M:%S"
#inicializando a variavel
#HrBanco = datetime.strptime('00:00:00', date_format)

#convertendo uma strinf para a hora
#HrEntrada  = datetime.strptime('08:30:00', date_format)
HrEntrada='08:30:00'
h, m, s = (map(int, HrEntrada.split(':')))
HrEntrada = datetime.timedelta(0,s,0,0,m,h)

#HrChegada1  = datetime.strptime('08:00:00', date_format)
HrChegada1='08:00:00'
h, m, s = (map(int, HrChegada1.split(':')))
HrChegada1 = datetime.timedelta(0,s,0,0,m,h)

#HrChegada2  = datetime.strptime('07:30:00', date_format)
HrChegada2='07:30:00'
h, m, s = (map(int, HrChegada2.split(':')))
HrChegada2 = datetime.timedelta(0,s,0,0,m,h)

#print('hora da Entrada :  ', HrEntrada)
#print('hora da Chegada1 :  ', HrChegada1)
#print('hora da Chegada2 :  ', HrChegada2)

listHrChegadas=[HrChegada1,HrChegada2]
listHrChegadas1=['08:00:00','07:30:00']

#----------------------------------------
# exemplo para mexer com horas.
#h, m, s = (map(int, time2.split(':')))
#time20 = datetime.timedelta(0,s,0,0,m,h)
#----------------------------------------

print('lista de chegadas: ',listHrChegadas)
print('lista de chegas 1: ', listHrChegadas1)

# @@@@@@ Função para covnerter Hora, minuto e segundos de uma forma mais elegante! @@@@@@@@
#def convert_timedelta(duration):
#    days, seconds = duration.days, duration.seconds hours = days * 24 + seconds // 3600
#    minutes = (seconds % 3600) // 60
#    seconds = (seconds % 60)
#    return hours, minutes, seconds

#td = datetime.timedelta(2, 7743, 12345)
#hours, minutes, seconds = convert_timedelta(td)
#print '{} minutes, {} hours'.format(minutes, hours)

VlrIndex=[]
HrBanco=[]
# CALCULA A DIFERENÇA ENTRE A HORA QUE ENTRO COM AS HORAS QUE CHEGUEI E GUARDA EM UMA LISTA
for horas in listHrChegadas1:
    #Encontrando a diferença entre as horas
    #print(HrEntrada)
    #print(h)
    h,m,s = (map(int, horas.split(':')))
    horas = datetime.timedelta(0,s,0,0,m,h)
    print('type variável horas: ',type(horas))
    Dif = HrEntrada - horas
    print('Total é :', Dif )
    HrBanco.append(Dif)


print('trecho de teste----------------------------')
n=HrBanco[0]
print('nnnnnnnnnn',n)
print("Tupla de Datetime: " + str(n))
print('fim de teste ----------------------------')



# LISTA COM OS HORAS/MINUTOS QUE FIZ DE BANCO
'''
aa=0
bb=0
tam = 0
for i in HrBanco:
    #print('Horas do Banco é: ', str(i))
    #h,m,s = (map(int, a.split(':')))
    #a.datetime.timedelta(0,s,0,0,m,h)
    #THrBanco =
    #tam = len(HrBanco)
    tam = tam+1
    if tam == 1:
        aa=i
    if tam == 2:
        bb=i

print('aaaaaaa: ', aa)
print('bbbbbbb: ', bb)
'''

print('HrBanco  ----------- ', HrBanco)

print('------------- AQUI QUE ESTOU SOMANDO CERTO ---------------')
soma=[]
soma.append(HrBanco[0]+HrBanco[1])
print(soma[0])
print('------------- FIMMMMMMMMM ---------------')


x=0
#while x < len(HrBanco):
somar=0
x=1
for x in HrBanco:
    print('print while x: ', x)
    #if x == 1:
    #    x1=HrBanco[x]
    #if x == 2:
    #    x2=HrBanco[x]
    #somar += x
    meux=x


print('------Imprimindo a Data e Hora Atual e separando Hora:Minuto:Segundos------')
now=datetime.datetime.now()
print(now.hour)     #print(now.day)
print(now.minute)   #print(now.mounth)
print(now.second)   #print(now.year)
print('------FIM------')

meux = datetime.timedelta(0,s,0,0,m,h)
h,m,s = (map(timedelta, meux.split(':')))

#print('type variável a: ',type(aa))
#c = int(a)+int(b)
#h,m,s = (map(int, aa.split(':')))
#aa = datetime.timedelta(0,s,0,0,m,h)
