import sys
#entrada = sys.stdin.readlines()
with open("arquivo.txt") as arquivo:
    entrada = arquivo.readlines()
#unica função do programa, realiza a junção e ordenação dos vizinhos
def vizinhanca(vertice):
  alcancados = set()
  fila = []
  fila.append(vertice)
  while len(fila) != 0:
    u = fila.pop(0)
    alcancados.add(u)
    for viz in lista_adjacencias[u-1]:
      if viz not in alcancados:
        fila.append(viz)
  return sorted(alcancados)
#
lista_entrada = []
for i in entrada:
  i = i.replace('\n','')
  lista_entrada.append(i)

lista_entrada.pop(0)
lista_entrada.pop(0)
lista_entrada.pop(1)  
num_vertices = (lista_entrada.pop(0))
num_vertices = int(num_vertices.replace('n=',''))
#
lista_vertices = [i for i in range(1,num_vertices+1)]
#
lista_arestas = []
for i, ver in enumerate(lista_entrada):
  aux = ver.split()
  a, b = int(aux[0]), int(aux[1])
  lista_arestas.append((a,b))
#
lista_adjacencias = [[] for i in range(num_vertices)]
for u, v in lista_arestas:
  lista_adjacencias[u-1].append(v)
  lista_adjacencias[v-1].append(u)
#
componentes = []
lista_check = [False for i in range(num_vertices)]
for i in range(num_vertices):
  if lista_check[i] == False:
    vizinhos = vizinhanca(i+1)
    if len(vizinhos) != 0:
      componentes.append(vizinhos)
    else:
      componentes.append([i+1])
    for aux in vizinhos:
      lista_check[aux - 1] = True
#
for i in range (len(componentes)):
  print(" ".join([str(x) for x in componentes[i]]))