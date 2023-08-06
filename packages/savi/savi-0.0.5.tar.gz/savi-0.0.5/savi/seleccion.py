import numpy as np 
#USAR CON PRECAUCIÓN XD
def seleccion(vec,dim):
    i=0
    while i < dim - 1:
        a=i
        b=i+1
        while b < dim:
            if vec[b] < vec[a]:
                a=b
            b=b+1
        aux=vec[a]
        vec[a]=vec[i]
        vec[i]=aux
        i=i+1

def seleccionAlgoritmo():
    print("\n\tALGORITMO DE ORDENACIÓN POR MÉTODO DE SELECCIÓN\n")
    algoritmo="INICIO\ni=0\nwhile i < dim - 1:\n\ta=i\n\tb=i+1\n\twhile b < dim:\n\t\tif vec[b] < vec[a]:\n\t\t\ta=b\n\t\tb=b+1\n\taux=vec[a]\n\tvec[a]=vec[i]\n\tvec[i]=aux\n\ti=i+1\nFIN\n"
    print(algoritmo)