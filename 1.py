def comprobar(n):
    if(n>=1 and n<=20):
        return 1
    else:
        return 0
def cLista(n):
    lista = [6, 14, 11, 3, 2, 1, 15, 19]
    for i in lista:
        if(n==i):
            return 1
n = int(input("Ingrese un número entre 1 y 20: "))
if(comprobar(n)==1):
    if(cLista(n)==1):
        print("Está dentro de la lista")
    else:
        print("No está dentro de la lista")
else:
    print("El número no está en el rango")
