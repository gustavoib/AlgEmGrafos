import sys
#função para achar os vizinhos de um vertice
def AcharVizinhos(v):
    alcancados = set()
    fila = []
    fila.append(v)
    while len(fila) != 0:
        u = fila.pop(0)
        alcancados.add(u)
        for i in lista_adjacencias[u-1]:
            if i not in alcancados:
                fila.append(i)
    return sorted(alcancados)
#recebendo arquivo de entrada

entrada = sys.stdin.readlines()
#extraindo dados importantes(numero de vertices e arestas)
conteudo = [dado.strip('\n') for dado in entrada]
n = int(conteudo.pop(2).replace('n=',''))
del conteudo[:3]
#criar vertices
vertices = [i+1 for i in range(n)]
#criar arestas
arestas = []
for i, linha in enumerate(conteudo):
    aux = linha.split()
    a, b = int(aux[0]), int(aux[1])
    arestas.append({a,b})
#criar lista de adjacencias
lista_adjacencias = [[] for i in range(n)]
for u, v in arestas:
    lista_adjacencias[u-1].append(v)
    lista_adjacencias[v-1].append(u)
#impressão das componentes
comp_conexas = []
lista_aux = [False]*n
for i in range(n):
    if lista_aux[i] == False:
        vizinhos = AcharVizinhos(i+1)
        for i in vizinhos:
            lista_aux[i-1] = True
    else:
        continue  
    print(' '.join(map(str, vizinhos)))        
