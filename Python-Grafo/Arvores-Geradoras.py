
import numpy as np


class Grafo:
    
    def __init__(self):
        self.vertices = []
        self.arestas = {}
        self.pesos = {}
        
    def adiciona_vertice(self, valor):
        
        self.vertices.append(valor)
        self.arestas[valor] = []
        
    def adiciona_aresta(self, origem, destino, peso):
        
        if origem not in self.vertices:
            self.adiciona_vertice(origem)
            
        if destino not in self.vertices:
            self.adiciona_vertice(destino)
        
        self.arestas[origem].append(destino)
        self.arestas[destino].append(origem)
        
        self.pesos[(origem,destino)] = peso
        self.pesos[(destino,origem)] = peso
        
        
def menor_vertice(vertices, distancias):

    menor_vertice   = None
    menor_distancia = None

    for vertice in vertices:

        if menor_vertice is None or distancias[vertice] < menor_distancia:
            menor_vertice = vertice
            menor_distancia = distancias[vertice]

    
    return menor_vertice



def prim(grafo, origem):

    pesos = {}
    E = {}
    temporario = []
    vertices = grafo.vertices

    for v in vertices:
        pesos[v] = np.inf

    pesos[origem] = 0
    E[origem] = {}

    while len(vertices) > 0:

        MenorVertice = menor_vertice(vertices, pesos)
        temporario.append(E[MenorVertice])
        vertices.pop(vertices.index(MenorVertice))

        for x in grafo.arestas[MenorVertice]:

            if x in vertices and grafo.pesos[(MenorVertice, x)] < pesos[x] :
                pesos[x] = grafo.pesos[(MenorVertice, x )]
                E[x] = {(MenorVertice, x)}

    return temporario
   
    
def ArvoreGeradoraSimples(grafo, inicio):
    
    visitados = []
    
    fila = [inicio]
    visitados = [inicio]
    
    while len(fila) > 0:
        u = fila.pop(0) 
    
        for v in grafo.arestas[u]: # pra cada adjacencia u---v
            if v not in visitados:
                
                visitados.append(v)
                fila.append(v)
    
    return visitados
    
    
def menorRota(mapa, origem):

    
    caminho = ArvoreGeradoraSimples(mapa, origem)
    #caminho = prim(mapa, origem)

    
    return caminho
    

###############

g = Grafo()

# rotas terrestres

g.adiciona_aresta("Fallarbor", "Mauville", 19)
g.adiciona_aresta("Fallarbor", "Rustboro", 9)
g.adiciona_aresta("Fortree", "Lilycove", 7)
g.adiciona_aresta("Fortree", "Mauville", 9)
g.adiciona_aresta("Mauville", "Verdanturf", 2)
g.adiciona_aresta("Mauville", "Slateport", 8)
g.adiciona_aresta("Oldale", "Petalburg", 2)
g.adiciona_aresta("Petalburg", "Rustboro", 6)
g.adiciona_aresta("Rustboro", "Verdanturf", 4)
g.adiciona_aresta("Dewford", "Pacifidlog", 16)
g.adiciona_aresta("Fortree", "Pacifidlog", 14)
g.adiciona_aresta("Lavaridge", "Mauville", 6)
g.adiciona_aresta("Lilycove", "Mauville", 14)
g.adiciona_aresta("Mauville", "Pacifidlog", 12)
g.adiciona_aresta("Mossdeep", "Pacifidlog", 14)
g.adiciona_aresta("Petalburg", "Verdanturf", 7)
g.adiciona_aresta("Dewford", "Petalburg", 9)
g.adiciona_aresta("Dewford", "Slateport", 20)
g.adiciona_aresta("Ever Grand", "Lilycove", 13)
g.adiciona_aresta("Ever Grand", "Pacifidlog", 15)
g.adiciona_aresta("Ever Grand", "Sootopolis", 12)
g.adiciona_aresta("Lilycove", "Mossdeep", 6)
g.adiciona_aresta("Lilycove", "Sootopolis", 6)
g.adiciona_aresta("Littleroot", "Oldale", 5)
g.adiciona_aresta("Mossdeep", "Sootopolis", 8)
g.adiciona_aresta("Pacifidlog", "Slateport", 11)
g.adiciona_aresta("Pacifidlog", "Sootopolis", 17)


caminho = menorRota(g, "Fallarbor" )
                            
print(caminho)

