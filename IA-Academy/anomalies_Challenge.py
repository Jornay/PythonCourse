

#=========================
# Desafio 1 - Liga acadêmica de inteligência artificial
# Considere a seguinte lista de valores e adicione no vetor anomalias,
# os valores que seu algoritmo considerar muito diferente dos outros.
# A definição de anomalia e uma estratégia para tratar dela faz parte
# do desafio e você deve pesquisar para adquirir conhecimento.
#=========================

#=========================
# Utilizando o método de detecção de anomalias
# Z-Score
# fonte : https://blog.dp6.com.br/m%C3%A9todos-de-detec%C3%A7%C3%A3o-de-anomalias-7daca729c27
#=========================


#===============================Program=====================================
#===========================================================================

import math


valores = [8, 9, 11, 12, 13, 16, 10, 5, 9, 12, 11, 8, 9, 11, 12, 15]

def _mean(data):
    
    aux = 0
    for i in data:
        aux = aux + i  

    return (aux / len(data))


def _desvPadrao(data, media):
    
    qtdeData = len(data)
    somatoria = 0     
    

    for i in data:
        somatoria =  somatoria + ( (i - media) ** 2 )
   
    return ( math.sqrt( somatoria / qtdeData ) )
    


def zScore(data, desvPadrao, media):

    values = []
    aux = 0 

    for i in data:
        
        aux = ((i - media) / desvPadrao)
        values.append(aux)
    
    return values
    

media = _mean(valores)

desvPadrao = _desvPadrao(valores, media)

values = zScore(valores, desvPadrao, media)


posicoes = []
cont = 0
for i in values:
    
    if i < -1 or i > 1:
        posicoes.append(cont)
    cont += 1

for i in posicoes:
    print("valor = ", valores[i] ," na posicao = [", i , "] do vetor" )


#===========================================================================






