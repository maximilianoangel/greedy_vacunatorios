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
        while i < 11:
            aux = mejor[0].copy()
            if aux[i] == 0:
                aux[i] = 1
                if sol(aux) == 1 and FO(aux) < mejor[1]: # si el elemento del vecinadario es una solucion factible y tiene menor valor en su funcion objetivo, se cambia de solucion
                    mejor = [aux.copy(), FO(aux)]
                    break
            else:
                aux[i] = 0
                if sol(aux) == 1 and FO(aux) < mejor[1]: # si el elemento del vecinadario es una solucion factible y tiene menor valor en su funcion objetivo, se cambia de solucion
                    mejor = [aux.copy(), FO(aux)]
                    break
            i += 1
        break # Para salir del while true
    print(f"La solucion final de la iteracion {iteracion} es {mejor[0]} con FO {mejor[1]}")
    

soluciones_greedy=[[1,0,1,0,0,1,1,1,1,0,1],[0,1,1,0,1,0,0,0,1,0,0],[0,0,1,1,1,0,1,0,1,0,1],[0,1,0,0,0,1,0,0,0,1,0],[0,0,1,1,1,0,1,0,0,1,1],[0,1,0,0,1,0,0,0,1,0,1],[1,1,0,0,0,0,1,0,1,1,0],
[0,1,0,0,0,1,1,0,0,0,0],[0,1,0,0,1,0,1,0,1,1,1],[0,0,1,1,0,0,1,0,0,1,0],[0,1,1,0,0,0,0,1,0,0,1],[0,0,0,1,0,0,0,0,1,1,0],[0,0,0,1,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,1,0,0,1],[0,0,1,1,0,1,0,1,1,1,0],
[0,0,0,1,0,0,0,0,1,0,1],[1,0,1,0,0,0,1,0,0,1,0],[0,1,1,0,0,1,0,1,1,0,0],[1,0,1,0,0,0,0,1,0,1,1],[0,1,1,0,0,0,1,0,1,0,0]]

i=0
while i<len(soluciones_greedy):
    hill_climbing(soluciones_greedy[i],i+1) 
    i=i+1