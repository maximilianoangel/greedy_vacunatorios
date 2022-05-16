from pickle import TRUE
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
prob=[] #arreglo donde se calcularan las probabilidades
def FO(X):#Calcula funcion objetivo
    i=0
    aux=0
    while i<11:
        aux=C[i]*X[i]+aux
        i=i+1
    return aux

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
def cambio(aux,indice):#movimiento del hill-climbing
    if aux[indice]==0:
        aux[indice]=1
    else:
        aux[indice]=0
    return aux
def limpiar(aux):#vacia las listas vecindad y prob
    i=0
    largo=len(aux)
    while largo>i:
        aux.pop()
        i=i+1

def probabilidad(inicial,final): #establece la probabilidad de cada posible solucion, segun su FO
    aux=((inicial-final)/inicial)*100
    if aux<0:
        return int(aux*(-1))
    else:
        aux=aux/2
        return int(aux)
def ListaProb(aux):#crea un arreglo donde se llevara acabo la ruleta
    aux2=[]
    largo=len(aux)
    i=0
    indice=0
    while i<largo:
        indice=0
        j=aux[i]
        while indice<j:
            aux2.append(i)
            indice=indice+1
        i=i+1
    return aux2
def hill_climbing(solu,iteracion,it):
    mejor=[solu[:],FO(solu)]#mejor resultado
    actual=solu[:]
    siguiente=solu[:]
    vecindad=[]
    semilla=1
    print("La solucion inicial de la iteracion "+str(it)+ " es: " +str(mejor[0])+ " con una FO: "+str(mejor[1]))
    while True:
        i=0
        j=0
        while i<11:
            if sol(cambio(actual[:],i))==1:#llena la vecindad solo con posibles soluciones, si no es posible solucion, se descarta
                vecindad.append(cambio(actual[:],i))
                prob.append(probabilidad(FO(actual),FO(vecindad[j])))
                j=j+1
            i=i+1
        ListaProb(prob)#crea la lista donde se llevara acabo la ruleta
        random.seed(semilla+iteracion)
        aux=random.randint(1,len(prob))#se elige la posicion de la ruleta
        if mejor[1]>=FO(vecindad[aux-1]):#se actualiza el mejor resultado
            siguiente=vecindad[aux-1]
            mejor=[siguiente[:],FO(siguiente)]
        actual=vecindad[aux-1]
        limpiar(prob)
        limpiar(vecindad)
        semilla=semilla+1
        if semilla==21:#termina el hill-climbing en la iteracion 20
            break
    print("La mejor solucion encontrada de la iteracion " + str(it) + " es: "+str(mejor[0])+ " con una FO: "+str(mejor[1]) )
    return iteracion+semilla #se utilizara para explorar soluciones en las proximas entradas
        
soluciones_greedy=[[1,0,1,0,0,1,1,1,1,0,1],[0,1,1,0,1,0,0,0,1,0,0],[0,0,1,1,1,0,1,0,1,0,1],[0,1,0,0,0,1,0,0,0,1,0],[0,0,1,1,1,0,1,0,0,1,1],[0,1,0,0,1,0,0,0,1,0,1],[1,1,0,0,0,0,1,0,1,1,0],
[0,1,0,0,0,1,1,0,0,0,0],[0,1,0,0,1,0,1,0,1,1,1],[0,0,1,1,0,0,1,0,0,1,0],[0,1,1,0,0,0,0,1,0,0,1],[0,0,0,1,0,0,0,0,1,1,0],[0,0,0,1,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,1,0,0,1],[0,0,1,1,0,1,0,1,1,1,0],
[0,0,0,1,0,0,0,0,1,0,1],[1,0,1,0,0,0,1,0,0,1,0],[0,1,1,0,0,1,0,1,1,0,0],[1,0,1,0,0,0,0,1,0,1,1],[0,1,1,0,0,0,1,0,1,0,0]]
i=0
aux=0
while i<len(soluciones_greedy):
    aux=hill_climbing(soluciones_greedy[i],aux+i,i+1)+aux #aux sirve para dispersar las semillas.
    i=i+1