def grafo():
    N, A ,B = map(lambda i: int(i), input().split(' '))
    grafo = [[] for a in range(N)]
    for a in range(N-1):
        P, Q, D = map(lambda i: int(i), input().split(' '))
        grafo[P-1].append((Q-1, D))
        grafo[Q-1].append((P-1, D))
        
    distancia(grafo, A-1, B-1)

def distancia(grafo, inicio, fim):
    visitados = [0 for b in range(len(grafo))]
    fila = []
    atual = inicio
    visitados[atual] = 1
    for x in grafo[atual]:
        if visitados[x[0]] == 0:
            visitados[x[0]] = 1
            fila.append(x)
    atual = fila.pop(0)
    
    while atual[0] != fim:
        for x in grafo[atual[0]]:
            if visitados[x[0]] == 0:
                visitados[x[0]] = 1
                fila.append((x[0], x[1]+atual[1]))
                

        atual = fila.pop(0)
    return print(atual[1])

grafo()
