# coding: utf-8
from datetime import datetime, timedelta
import datetime

'''
MAIO - 2021
=>06/05/2021:  Entrada as '08:11:00' ---
=>07/05/2021:  Entrada as '08:12:00' ---
=>10/05/2021:  Entrada as '08:00:00' ---
=>11/05/2021:  Entrada as '08:14:00' ---
=>12/05/2021:  Entrada as '08:16:00' ---
=>13/05/2021:  Entrada as '08:15:00' ---
=>18/05/2021:  Entrada as '08:10:00' ---
=>19/05/2021:  Entrada as '08:05:00' ---
=>20/05/2021:  Entrada as '08:12:00' ---
=>21/05/2021:  Entrada as '08:02:00' ---
=>24/05/2021:  Entrada as '08:01:00' ---
=>25/05/2021:  Entrada as '08:23:00' ---
=>25/05/2021:  Entrada as '08:03:00' ---

                         -----------
TOTAL ATÉ O MOMENTO DE: |  4:26:00  | ***## Anotações:    ##***
                         -----------
'''


from datetime import datetime, timedelta
import datetime



HrEntrada = '08:30:00' # Meu Horário de Entrada
h, m, s = (map(int, HrEntrada.split(':')))
HrEntrada = datetime.timedelta(0,s,0,0,m,h)

# Lista com Horários que ENTREI mais CEDO na Empresa
listHrChegadas=['08:11:00','08:12:00','08:00:00','08:14:00','08:16:00','08:15:00','08:10:00','08:05:00','08:12:00',
				'08:02:00','08:01:00','08:23:00','08:03:00',]


HrSaida = '17:30:00' # Meu Horário de Saída
h, m, s = (map(int, HrSaida.split(':')))
HrSaida = datetime.timedelta(0,s,0,0,m,h)

# Lista com Horários que SAÍ mais TARDE na Empresa
listaHrSaidas=['00:00:00']

lsCalculaDifEntrada = [] # Lista que será adicionado as Diferenças da entrada
lsCalculaDifSaida = [] # Lista que será adicionado as Diferenças da Saída

HrBanco=[] # Lista que será adicionado as Diferenças

#@@@@@@   CALCULA ENTRADA @@@@@@@
# CALCULA A DIFERENÇA ENTRE A HORA QUE ENTRO COM AS HORAS QUE CHEGUEI E GUARDA EM UMA LISTA

for lhoras in listHrChegadas:
    #Encontrando a diferença entre as horas
    h,m,s = (map(int, lhoras.split(':')))
    lhoras = datetime.timedelta(0,s,0,0,m,h)
    #print('type variável horas: ',type(horas))
    if listHrChegadas[0] != '00:00:00': # Se houver horario de entrada calculo a diferença
        Dif = HrEntrada - lhoras
    else:
        Dif = lhoras
    #print('Total é :', Dif )
    lsCalculaDifEntrada.append(Dif)

somaEntrada=[]
tam=len(lsCalculaDifEntrada)
# print(tam)
x=0
while x < tam:
    #print(x)
    if x == 0:
        l = lsCalculaDifEntrada[x]
    if x > 0:
        l += +lsCalculaDifEntrada[x]
    x+=1
#print('valor de l é :   ', l)
somaEntrada.append(l)

if listHrChegadas[0] != '00:00:00':
    print('-------------------------------------------------------------------')
    print('|                     Calulando Horas Entradas                     |          ')
    print('-------------------------------------------------------------------|         |')
    print('Total de Horas Pagas que fiz antes das 08:30 até o momento foi de:  ', somaEntrada[0],  ' *** ##ANOTAÇÔES ENTRADAS: ##***')
    print('-------------------------------------------------------------------|         |')
    print()
    print()

#@@@@@@   CALCULA SAIDA  @@@@@@@
# CALCULA A DIFERENÇA ENTRE A HORA QUE SAIO COM AS HORAS QUE SAÍ E GUARDA EM UMA LISTA

if listaHrSaidas[0] != '00:00:00': # Se estiver com valor '00:00:00' é por que não tive Horas extras depois das 17:30.
    for lhoras in listaHrSaidas:
        #Encontrando a diferença entre as horas
        h,m,s = (map(int, lhoras.split(':')))
        lhoras = datetime.timedelta(0,s,0,0,m,h)
        #print('type variável horas: ',type(horas))
        Dif = lhoras - HrSaida
        #print('Total é :', Dif )
        lsCalculaDifSaida.append(Dif)

    somaSaida=[]
    tam=len(lsCalculaDifSaida)
    #print(tam)
    x=0
    while x < tam:
        #print(x)
        if x == 0:
            l = lsCalculaDifSaida[x]
        if x > 0:
            l += +lsCalculaDifSaida[x]
        x+=1
    #print('valor de l é :   ', l)
    somaSaida.append(l)

if listaHrSaidas[0] != '00:00:00': # Se estiver com valor '00:00:00' é por que não tive Horas extras depois das 17:30.
    print('-------------------------------------------------------------------')
    print('|                     Calulando Horas Saídas                       |          ')
    print('-------------------------------------------------------------------|         |')
    print('Total de Horas Pagas que fiz depois das 17:30 até o momento foi de: ', somaSaida[0],  ' *** ## ANOTAÇÔES SAÍDAS: FIZ 2 horas Sábado 01/02/20, Projeto Educação ##***')
    print('-------------------------------------------------------------------|         |')

print()
print()
print()

if listaHrSaidas[0] != '00:00:00':
    print('-------------------------------------------------------------------')
    print('|                     TOTAL DE HORAS EXTRAS                        |          ')
    print('-------------------------------------------------------------------|         |')
    print('           TOTAL DE HORAS ANTES DA ENTRADA E DEPOIS DA SAÍDA :      ' ,somaEntrada[0] + somaSaida[0],  ' *** ## ANOTAÇÔES FINAIS: As Horas a mais que fiz, contando o que entrei antes e saí depois do meu horário ##***')
    print('-------------------------------------------------------------------|         |')
else:
    print('-------------------------------------------------------------------')
    print('|                     TOTAL DE HORAS EXTRAS                        |          ')
    print('-------------------------------------------------------------------|         |')
    print('           TOTAL DE HORAS ANTES DA ENTRADA E DEPOIS DA SAÍDA :      ' ,somaEntrada[0],  ' *** ## ANOTAÇÔES FINAIS:   ##***')
    print('-------------------------------------------------------------------|         |')
