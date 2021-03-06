A=[[1,1,1,1,0,0,0,0,0,0,0], #matriz con las comunas que se satisfacen al construir en cada comuna
[1,1,0,1,0,0,0,0,0,0,0],
[1,0,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,0,0,0,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,1,0,1,1,0,0,1,0,0],
[0,0,0,0,1,0,1,1,0,1,1],
[0,0,0,0,1,0,1,1,1,1,0],
[0,0,0,0,1,1,0,1,1,1,1],
[0,0,0,0,0,0,1,1,1,1,1],
[0,0,0,0,0,0,1,0,1,1,1]]


C=[60,30,60,70,130,50,70,60,50,80,40] #costos

def FO(X):#Calcula funcion objetivo
    i=0
    aux=0
    while i<11:
        aux=C[i]*X[i]+aux
        i=i+1
    return int(aux)

def min(vecindario, FOoriginal): # Busca el minimo del vecindario y que a su vez sea menor que el valor de la funcion objetivo de la original
    i = 0
    aux = [vecindario[0].copy(), FO(vecindario[0])]
    while i < len(vecindario):
        if FO(vecindario[i]) < aux[1]:
            aux = [vecindario[i].copy(), FO(vecindario[i])]
        i += 1
    if aux[1] < FOoriginal:
        return aux
    else:
        return [0, 0]

def sol(decision): #confirma si con los valores en X se satisface la restriccion
    j=0
    while j<11:
        i=0
        aux=0
        while i<11:
            aux=(A[i][j])*decision[i]+aux
            i=i+1
        if aux<1:
            return 0
        j=j+1
    return 1

def hill_climbing(solu, iteracion):
    mejor = [solu.copy(), FO(solu)]
    print(f"La solucion inicial de la iteracion {iteracion} es {mejor[0]} con FO {mejor[1]}")
    while True:
        i = 0
        vecindario = []
        while i < 11: # Llenado del vecindario, el movimiento es cambiar 0 por 1 y viceversa 
            aux = mejor[0].copy()
            if aux[i] == 0:
                aux[i] = 1
                if sol(aux) == 1:
                    vecindario.append(aux.copy())
            else:
                aux[i] = 0
                if sol(aux) == 1:
                    vecindario.append(aux.copy())
            i += 1
        proxima_solucion = min(vecindario.copy(), mejor[1]) # Busca el minimo del vecindario y que a su vez sea menor que el valor de la funcion objetivo de la original
        if proxima_solucion == [0, 0]:
            break
        else:
            mejor = [proxima_solucion[0].copy(), proxima_solucion[1]]
    print(f"La solucion final de la iteracion {iteracion} es {mejor[0]} con FO {mejor[1]}")
    

soluciones_greedy=[[1,0,1,0,0,1,1,1,1,0,1],[0,1,1,0,1,0,0,0,1,0,0],[0,0,1,1,1,0,1,0,1,0,1],[0,1,0,0,0,1,0,0,0,1,0],[0,0,1,1,1,0,1,0,0,1,1],[0,1,0,0,1,0,0,0,1,0,1],[1,1,0,0,0,0,1,0,1,1,0],
[0,1,0,0,0,1,1,0,0,0,0],[0,1,0,0,1,0,1,0,1,1,1],[0,0,1,1,0,0,1,0,0,1,0],[0,1,1,0,0,0,0,1,0,0,1],[0,0,0,1,0,0,0,0,1,1,0],[0,0,0,1,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,1,0,0,1],[0,0,1,1,0,1,0,1,1,1,0],
[0,0,0,1,0,0,0,0,1,0,1],[1,0,1,0,0,0,1,0,0,1,0],[0,1,1,0,0,1,0,1,1,0,0],[1,0,1,0,0,0,0,1,0,1,1],[0,1,1,0,0,0,1,0,1,0,0]]

i=0
aux=0
while i<len(soluciones_greedy):
    hill_climbing(soluciones_greedy[i],i+1)
    i=i+1