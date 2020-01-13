
from datetime import datetime, timedelta
import datetime

'''
Pagando Horas: !ZERADO!
=>04/10/2018 : entrei as '08:00:00'=>05/10/2018:  entrei as '08:00:00'=>08/10/2018:  entrei as '07:30:00'=>09/10/2018:  entrei as '07:30:00'=>10/10/2018:  entrei as '08:05:00'=>11/10/2019:  entrei as '07:45:00'=>15/10/2018:  entrei as '07:55:00'=>17/10/2018:  entrei as '07:44:00'=>18/10/2018:  entrei as '07:43:00'=>19/10/2018:  entrei as '07:27:00'=>22/10/2018:  entrei as '07:34:00'=>23/10/2018:  entrei as '07:17:00'=>24/10/2018:  entrei as '07:23:00'=>25/10/2018:  entrei as '08:00:00'
@@@ aqui até o momento paguei o que deveria que no caso é 12:00 @@@
                         -----------
TOTAL ATÉ O MOMENTO DE: | 12:10:00  | *** No relatorio da Softhouse diz que fiz apenas 07horas e pouco de Horas Extras ***
                         -----------
++++++ ZERADO ++++++
'''

'''
PAGANDO OUTRAS HORAS: !ZERADO!
=>29/11/2018:  entrei as '08:11:00'=>29/11/2018:  entrei as '08:12:00'=>04/12/2018:  entrei as '08:17:00'
Paguei 50 minutos, foi feito a conta e Evandro me disse que falta pagar somente 46 minutos
++++++ ZERADO ++++++

Pagar ... ainda falta 46 minutos
=>05/12/2018:  entrei as '08:14:00'=>06/12/2018:  entrei as '07:58:00'
++++++ ZERADO ++++++
'''

'''
Viagem que fiz para São Vicente sai de casa as 07:00 mas voltei era 18:20(acrescentar 50 minutos que equivale horario a mais que fiz depois do horario que saiu da Soft)
=>18/12/2018:  entrei as '07:52:00'=>19/12/2018:  entrei as '07:57:00'=>20/12/2018:  entrei as '08:08:00'=>26/12/2018:  entrei as '08:06:00'=>27/12/2018:  entrei as '08:13:00'=>28/12/2018:  entrei as '08:18:00'
Mês de Dezembro fiz 3:56:00 + 50 minutos = 4:46:00 que fiz depois do horario, qdo fui para são vicente.
++++++ ZERADO ++++++ Total de 4:46:00
'''

'''
FECHADO
Janeiro de 2019 Entradas:
=>02/01/2019:  entrei as '08:11:00'=>03/01/2019:  entrei as '08:00:00'=>07/01/2019:  entrei as '07:49:00'=>08/01/2019:  entrei as '07:29:00'=>10/01/2019:  entrei as '07:26:00'=>11/01/2019:  entrei as '07:43:00'=>14/01/2019:  entrei as '07:33:00'=>15/01/2019:  entrei as '07:36:00'=>16/01/2019:  entrei as '07:26:00'=>17/01/2019:  entrei as '07:35:00'=>18/01/2019:  entrei as '07:19:00'=>22/01/2019:  entrei as '07:37:00'=>23/01/2019:  entrei as '07:27:00'=>24/01/2019:  entrei as '07:27:00'=>28/012019:  entrei as '07:19:00'=>29/01/2019:  entrei as '07:26:00'=>30/01/2019:  entrei as '07:53:00'=>31/01/2019:  entrei as '07:37:00'
++++++ ZERADO ++++++ Total de 16:07:00
'''
'''
FEVEREIRO
=>01/02/2019:  entrei as '07:21:00' =>05/02/2019:  entrei as '07:20:00'  =>26/02/2019:  entrei as '07:22:00' =>28/02/2019:  entrei as '07:20:00'
++++++ ZERADO ++++++ Total de 04:37:00
'''

'''
DEZEMBRO
=>05/12/2019:  Entrada as '07:31:00'
=>06/12/2019:  Entrada as '08:08:00'
=>09/12/2019:  Entrada as '07:32:00'
=>10/12/2019:  Entrada as '07:43:00'
=>16/12/2019:  Saida as '20:58:00'
=>19/12/2019:  Entrada as '07:32:00' => Foi o dia em que foi passado o SIGS e Sisfarma para Nuvem (LocalWeb)
=>20/12/2019:  Entrada as '08:14:00'
=>23/12/2019:  Entrada as '07:32:00'
=>26/12/2019:  Entrada as '07:14:00'
=>27/12/2019:  Entrada as '07:53:00'
                         -----------
TOTAL ATÉ O MOMENTO DE: |  10:39:00   | ***## Anotações:  As Horas a mais que fiz, contando o que entrei antes e saí depois do meu horário  ##***
                         -----------
'''
'''
DEZEMBRO
=>08/01/2020:  Entrada as '06:53:00'
=>08/01/2020:  Saída as '17:43:00'
=>09/01/2020:  Entrada as '07:51:00'
=>09/01/2020:  Saída as '19:26:00'

                         -----------
TOTAL ATÉ O MOMENTO DE: |  4:25:00   | ***## Anotações:    ##***
                         -----------
'''


HrEntrada = '08:30:00' # Meu Horário de Entrada
h, m, s = (map(int, HrEntrada.split(':')))
HrEntrada = datetime.timedelta(0,s,0,0,m,h)

# Lista com Horários que ENTREI mais CEDO na Empresa
listHrChegadas=['06:53:00','07:51:00']

HrSaida = '17:30:00' # Meu Horário de Saída
h, m, s = (map(int, HrSaida.split(':')))
HrSaida = datetime.timedelta(0,s,0,0,m,h)

# Lista com Horários que SAÍ mais TARDE na Empresa

listaHrSaidas=['19:26:00','17:43:00']

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
    Dif = HrEntrada - lhoras
    #print('Total é :', Dif )
    lsCalculaDifEntrada.append(Dif)

somaEntrada=[]
tam=len(lsCalculaDifEntrada)
#print(tam)
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
    print('Total de Horas Pagas que fiz depois das 17:30 até o momento foi de: ', somaSaida[0],  ' *** ## ANOTAÇÔES SAÍDAS: ##***')
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
