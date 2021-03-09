


def reconheceGrafo(mapa):
    h, v , info = mapa['h'], mapa['v'], mapa['info']

    M = []
    V = {}

    #TRANSFORMA EM MATRIZ
    for linha in range(v):
        M.append([]) #M[] -> M[[]]

        for coluna in range(h):
            M[linha].append(info[linha * h + coluna])

    for i in M:
        print(i)
        
    direcoes = {
        '>' : (1,0),
        '<' : (-1,0),
        '^' : (0, -1),
        'v' : (0 , 1),
        '.' : (0, 0),
        '*' : (0 , 0)
    }
    
    linha, coluna = 0, 0
    
    simbolo = M[linha][coluna]
    ultimo_vertice = (linha, coluna)
    V[str(ultimo_vertice)] = []
    
    while simbolo != '*':
        
        #Verificar se atingiu o limite do mapa
        if coluna >= h or coluna < 0 or linha >= v or linha < 0:
            break  
        
        simbolo = M[linha][coluna]
        
        if simbolo != '.':
            dir_coluna , dir_linha = direcoes[simbolo]
            vertice_atual = (linha,coluna)
            
            if(ultimo_vertice != vertice_atual):
                
                #Verifica se o vertice ja não foi acionado    
                if str(vertice_atual) in V:
                    break
                
                V[ultimo_vertice].append(vertice_atual)
            
            ultimo_vertice = vertice_atual
            V[str(ultimo_vertice)] = []
        
        linha += dir_linha
        coluna += dir_coluna
        
        return M, V
    
def navegacao(M,V):
    posicao = (0,0)
    linha, coluna = posicao
    simbolo = M[linha][coluna]

    while simbolo != '*':
        adjacencias = V[str(posicao)]

        if len(adjacencias) <= 0:
            break

        posicao = adjacencias.pop()
        linha , coluna = posicao # (0,0) = 0   CONTUDO '(0,0)' ele não consegue atribuir apra as duas variaveis
        simbolo = M[linha][coluna]

    return simbolo


mapa4 = {'h': 10, 'v': 3, 'info': '>.....v..v>....*....^.....<..^'}


M, V  = reconheceGrafo(mapa4)
destino = navegacao(M,V)

print("SIMBOLO FINAL : ", destino)
if destino == '*':
    for i in M:
        print(i)

### mapa do maroto
### estrutura de dados 2

### utilize um mapa inicialmente, depois faça o código rodar em todos eles

""" Mapa 1
>....v
"""

mapa1 = {'h': 6, 'v': 1, 'info': '>....v'}

""" Mapa 2
>.....v
.......
v.....<
...*...
>......
"""

mapa2 = {'h': 7, 'v': 5, 'info': '>.....v.......v.....<...*...>......'}

""" Mapa 3
>.v.
....
*.v.
....
..^.
"""

mapa3 = {'h': 4, 'v': 5, 'info': '>.v.....*.v.......^.'}

""" Mapa 4
>.....v..v
>....*....
^.....<..^
"""

mapa4 = {'h': 10, 'v': 3, 'info': '>.....v..v>....*....^.....<..^'}


# DICAS:
#
# (1) pense como ler os dados do mapa e transformar em um grafo, (os mapas são dicionários) 
#     cada direção é um vértice e aponta com qual vértice seguinte se conecta
#
# (2) as arestas não devem ser utilizadas duas vezes para eles não se perderem no castelo
#
# (3) utilize papel e caneta para verificar se as informações de vértices e arestas estão corretas
#     a medida que você implementar
#
# (4) ao final, basta imprimir qual é o mapa CORRETO, para todos os outros apenas ignore

