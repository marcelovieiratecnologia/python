
from datetime import datetime, timedelta
import datetime
'''
Pagando Horas: !ACERTADO!
=>04/10/2018 : entrei as '08:00:00'
=>05/10/2018:  entrei as '08:00:00'
=>08/10/2018:  entrei as '07:30:00'
=>09/10/2018:  entrei as '07:30:00'
=>10/10/2018:  entrei as '08:05:00'
=>11/10/2019:  entrei as '07:45:00'
=>15/10/2018:  entrei as '07:55:00'
=>17/10/2018:  entrei as '07:44:00'
=>18/10/2018:  entrei as '07:43:00'
=>19/10/2018:  entrei as '07:27:00'
=>22/10/2018:  entrei as '07:34:00'
=>23/10/2018:  entrei as '07:17:00'
=>24/10/2018:  entrei as '07:23:00'
=>25/10/2018:  entrei as '08:00:00'

@@@ aqui até o momento paguei o que deveria que no caso é 12:00 @@@
                         -----------
TOTAL ATÉ O MOMENTO DE: | 12:10:00  | *** No relatorio da Softhouse diz que fiz apenas 07horas e pouco de Horas Extras ***
                         -----------
'''

'''
PAGANDO OUTRAS HORAS: !ACERTADO!
=>29/11/2018:  entrei as '08:11:00'
=>29/11/2018:  entrei as '08:12:00'
=>04/12/2018:  entrei as '08:17:00'
Paguei 50 minutos, foi feito a conta e Evandro me disse que falta pagar somente 46 minutos

...


Pagar ... ainda falta 46 minutos
=>05/12/2018:  entrei as '08:14:00'
=>06/12/2018:  entrei as '07:58:00'
++++++ ZERADO ++++++

'''

'''
Viagem que fiz para São Vicente sai de casa as 07:00 mas voltei era 18:20(acrescentar 50 minutos que equivale horario a mais que fiz depois do horario que saiu da Soft)
=>18/12/2018:  entrei as '07:52:00'
=>19/12/2018:  entrei as '07:57:00'
=>20/12/2018:  entrei as '08:08:00'
=>26/12/2018:  entrei as '08:06:00'
=>27/12/2018:  entrei as '08:13:00'
=>28/12/2018:  entrei as '08:18:00'
=>02/01/2019:  entrei as '08:11:00'
=>03/01/2019:  entrei as '08:00:00'
=>07/01/2019:  entrei as '07:49:00'
=>08/01/2019:  entrei as '07:29:00'
=>10/01/2019:  entrei as '07:26:00'
=>10/01/2019:  entrei as '07:43:00'

                         -----------
TOTAL ATÉ O MOMENTO DE: | 8:18:00   | ***  ***
                         -----------
'''

HrEntrada='08:30:00' # Meu Horário de Entrada
h, m, s = (map(int, HrEntrada.split(':')))
HrEntrada = datetime.timedelta(0,s,0,0,m,h)

# Horários que entrei mais cedo na Empresa
listHrChegadas1=['07:00:00','07:52:00','07:57:00','08:08:00','08:06:00',
                 '08:13:00','08:18:00','08:11:00','08:00:00','07:49:00',
                 '07:29:00','07:26:00','07:43:00']

HrBanco=[] # Lista que será adicionado as Diferenças
# CALCULA A DIFERENÇA ENTRE A HORA QUE ENTRO COM AS HORAS QUE CHEGUEI E GUARDA EM UMA LISTA
for lhoras in listHrChegadas1:
    #Encontrando a diferença entre as horas
    h,m,s = (map(int, lhoras.split(':')))
    lhoras = datetime.timedelta(0,s,0,0,m,h)
    #print('type variável horas: ',type(horas))
    Dif = HrEntrada - lhoras
    #print('Total é :', Dif )
    HrBanco.append(Dif)

soma=[]
tam=len(HrBanco)
#print(tam)
x=0
while x < tam:
    #print(x)
    if x == 0:
        l = HrBanco[x]
    if x > 0:
        l += +HrBanco[x]
    x+=1
#print('valor de l é :   ', l)
soma.append(l)
print('------------------------------------------|         |')
print('Total de Horas Pagas até o momento foi de: ', soma[0],  ' *** Somar 50 minutos que fiz depois do horario ***')
print('------------------------------------------|         |')
