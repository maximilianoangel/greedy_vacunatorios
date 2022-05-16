import random

A=[[1,1,1,1,0,0,0,0,0,0,0], #matriz con las comunas que se satisfacen al construir en cada comuna
[1,1,0,1,0,0,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
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
def sumaI(A,indice): #suma cuantas comunas se satisfacen al construir un vacunatorio
    aux=0
    j=0
    while j<11:
        aux=aux+A[indice][j]
        j=j+1
    return aux
def probabilidad(prob,costo,A):
    i=0
    while i<11:
        proba=int(costo[i]/sumaI(A,i)) #cuanto vale cubrir una comuna al construir en i
        if proba==18:
            proba=5
        elif proba==15:
            proba=7
        elif proba==14:
            proba=8
        elif proba==16:
            proba=6
        elif proba==12:
            proba=9
        elif proba==8:
            proba=18
        prob.append(int(proba))
        i=i+1
def ruleta(eleccion):
    prob=[1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,6,7,8,9,10,11,1,2,3,4,6,7,8,9,11,2,3,4,6,7,8,9,11,2,3,6,8,9,11,2,3,9,11,9,9,9,9,9,9,9,9]
    aux=prob[eleccion-1]
    return aux-1
def greedy(iteracion,it):
    semilla=1
    i=1
    while True:
        random.seed(semilla+iteracion)
        aux=random.randint(1,100)
        aux=ruleta(aux) #decide en que comuna se construira el consultorio
        X[aux]=1
        if sol(X) == 1:
            break
        else:
            semilla=semilla+1
            i=i+1
    print("solucion en la iteracion " + str(it) + ": " + str(X))
    aux=0
    while aux<11: #limpia la variable X
        X[aux]=0
        aux=aux+1
    return i

probabilidad(prob,C,A)
print(prob)
i=0
aux=0
while i<20:
    aux=greedy(i+aux,i+1) #aux sirve para dispersar las semillas.
    i=i+1