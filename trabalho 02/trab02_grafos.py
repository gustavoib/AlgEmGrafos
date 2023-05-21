import sys

'''with open ("arquivo_entrada.txt", "r") as arquivo:
    entrada = arquivo.readlines()'''

#chamada dos dados  
entrada = sys.stdin.readlines()

#extração do número de vértices do grafo em questão
n = int(entrada[2].split("=")[1])

class Vertice:
    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

class Componente:
    def __init__(self, primeiro, ultimo, tamanho):
        self.primeiro = primeiro
        self.ultimo = ultimo
        self.tamanho = tamanho

def ordenarArestasPeso(entrada):
    arestas = []
    for i in entrada[4:]:
        entrada = i.replace("\n", "")
        v1 = float(entrada.split(" ")[0])
        v2 = float(entrada.split(" ")[1])
        w = float(entrada.split(" ")[2]) # w = peso
        arestas.append([int(v1)-1,int(v2)-1,w])

    arestas_ordenadas = sorted(arestas, key=lambda x: x[2:])
    return arestas_ordenadas

def calcularPesoAGM():
    L = ordenarArestasPeso(entrada)
    contarArestas = 0
    pesoAGM = 0
    rep = list(range(n))
    comp = list(range(n))
    for u in range(n):
        primeiro = Vertice(u, None)
        ultimo = primeiro
        comp[u] = Componente(primeiro,ultimo,1)
    for aresta in L:
        u = aresta[0]
        v = aresta[1]
        if rep[u] != rep[v]:
            contarArestas += 1
            pesoAGM += aresta[2]
            x = rep[u]
            y = rep[v]
            if comp[x].tamanho < comp[y].tamanho:
                cp_x = x
                x = y
                y = cp_x
            z = comp[y].primeiro
            comp[x].ultimo.proximo = z
            comp[x].ultimo = comp[y].ultimo
            comp[x].tamanho += comp[y].tamanho
            while z:
                rep[z.valor] = x
                z = z.proximo
        if contarArestas == n-1:
            break
    return pesoAGM

#impressão do peso da AGM
peso = calcularPesoAGM()
print(f"{peso:.3f}")
