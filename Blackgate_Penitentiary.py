#Blackgate Penitentiary
#Bautista Castilla Cesar

import sys

entrada = sys.stdin.read() 
lineas = entrada.splitlines() 
n=int(lineas[0])
L=[]
i=1
while i<n+1:
    r=lineas[i].split()
    L.append({"Nombre":r[0],"Estatura":r[1]})
    i+=1


def funcionDic(e):
    return e["Estatura"]
    
L.sort(key=funcionDic)


i=0
ini=1
fin=1
LAUX=[]
while i<n-1:
    LAUX.append(L[i]["Nombre"])
    if(L[i]["Estatura"]!=L[i+1]["Estatura"]):
        LAUX.sort()
        for p in LAUX:
            print(p,end=" ")
        print(ini,fin)
        fin+=1
        ini=fin
        LAUX=[]
    else:
        fin+=1
        
    i+=1

LAUX.append(L[i]["Nombre"]) 
LAUX.sort()
for p in LAUX:
    print(p,end=" ")
print(ini,fin)
    
    