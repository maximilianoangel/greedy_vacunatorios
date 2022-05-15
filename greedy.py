A=[[1,1,1,1,0,0,0,0,0,0,0],
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

C=[60,30,60,70,130,50,70,60,50,80,40]
X=[0,0,0,0,0,0,0,0,0,0,0,]
prob=[]
def sol(decision):
    j=0
    while j<11:
        i=0
        aux=0
        while i<11:
            aux=(A[i][j]+aux)*decision[i]
            i=i+1
        if aux<1:
            return 0
        j=j+1
    return 1
def sumaI(A,indice):
    j=0
    aux=0
    while j<11:
        aux=aux+A[indice][j]
        j=j+1
    return aux
def probabilidad(prob,costo,A):
    i=0
    j=0
    while i<11:
        proba=int(costo[i]/sumaI(A,i)) #coste por comuna satisfecha
        if proba==18:
            proba=5
        elif proba==15:
            proba=13
        elif proba==14:
            proba=7
        elif proba==16:
            proba=6
        elif proba==12:
            proba=9
        elif proba==8:
            proba=14
        prob.append(int(proba))
        i=i+1

probabilidad(prob,C,A)
print(prob)
