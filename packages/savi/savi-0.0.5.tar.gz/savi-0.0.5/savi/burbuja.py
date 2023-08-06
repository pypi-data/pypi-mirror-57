import numpy as np
#USAR CON PRECAUCIÓN XD
def burbuja(vec,dim):
    bandera=True
    while bandera==True:
        bandera=False
        for i in range(0,dim-1):
            if vec[i]>vec[i+1]:
                aux=vec[i]
                vec[i]=vec[i+1]
                vec[i+1]=aux
                bandera=True

def burbujaAlgoritmo():
    print("\n\tALGORITMO DE ORDENACIÓN POR INTERCAMBIO O BURBUJA\n")
    algoritmo="INICIO\nbandera=True\nwhile bandera==True:\n\tbandera==False\n\tfor i in range(o,dimension-1):\n\t\tif vector[i]>vector[i+1]:\n\t\t\tauxiliar=vector\n\t\t\tvector[i]=vector[i+1]\n\t\t\tvector[i+1]=auxiliar\n\t\t\tbandera=True\nFIN\n"
    print(algoritmo)

