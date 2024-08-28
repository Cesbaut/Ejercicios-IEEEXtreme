# Ejercicio Lucky_days

# Bautista Castilla Cesar
# Franco Arellano Luis Fernando (Alias el Yoggy)
# Hector ...


def lucky(n,arreglo):
    
 
    i = 1
    mayor= arreglo[0]
    
    for j in range(1, n):
        if(arreglo[j]>mayor):
            mayor=arreglo[j]
            i+=1
    print(i)


import sys

entrada = sys.stdin.read() 
lineas = entrada.splitlines()

n = int(lineas[0])
arreglo=[]

numeros = lineas[1].split()
for op in numeros:
    arreglo.append(int(op))


lucky(n,arreglo)