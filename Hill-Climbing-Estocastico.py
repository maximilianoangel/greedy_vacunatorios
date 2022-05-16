import random

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
X=[0,0,0,0,0,0,0,0,0,0,0,] #variable de decision
prob=[] #arreglo donde se calcularan las probabilidades
def FO(X,indice):#Calcula funcion objetivo
    i=0
    aux=0
    while i<11:
        aux=C[i]*X[i]+aux
        i=i+1
    print("La solucion de la iteracion " +str(indice) +" tiene un valor de FO: "+str(aux))

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