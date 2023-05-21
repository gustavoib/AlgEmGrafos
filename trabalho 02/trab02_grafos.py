import sys

class Vertice:
    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

class Componente:
    def __init__(self, primeiro, ultimo, tamanho):
        self.primeiro = primeiro
        self.ultimo = ultimo
        self.tamanho = tamanho

def ordenarArestas(Grafo):
    if len(Grafo) <= 1:
        return Grafo
    else:
        pivo = Grafo[-1]
        menor = [x for x in Grafo[:-1] if x[2] <= pivo[2]]
        maior = [x for x in Grafo[:-1] if x[2] > pivo[2]]
        return ordenarArestas(menor) + [pivo] + ordenarArestas(maior)

def calcularPesoAGM(G,n):
    L = ordenarArestas(G)
    contarArestas = 0
    pesoAGM = 0
    rep = list(range(n+1))
    comp = [None] * n
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


if __name__ == "__main__":
    conteudo = sys.stdin.readlines()

    n = int(conteudo[2].split('=')[1])
    grafo = []

    for linha in conteudo[4:]:
        v1, v2, peso = map(float, linha.split())
        grafo.append([int(v1) - 1, int(v2) - 1, peso])

    tamanho = calcularPesoAGM(grafo, n)
    print(f"{tamanho:.3f}")
