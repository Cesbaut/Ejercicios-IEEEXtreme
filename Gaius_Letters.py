palabra = input()

resultado = ''
for letra in palabra:
    ascci = ord(letra)
    if (96<ascci<123):
        r = ascci-97
        if r<12:
            i = 123-(12-r)
        else:
            i=ascci-12
        resultado += chr(i)
    elif (64<ascci<91):
        r=ascci-65
        if r<12:
            i=91-(12-r)
        else:
            i=ascci-12
        resultado += chr(i)
    else:
        resultado += letra

print(resultado)