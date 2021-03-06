#Las list son colecciones ordenadas e intercambiables y que permite elementos duplicados

lista = ["manzana", "pera", "frambuesa"]
print(lista)
print("Longitud de la lista es de: ", len(lista))

list2 = [1, 5, 3, 9]
list3 = [True, False, False]
list4 = ["string", 24, True, 32, "cosa"]

print("Tipo de dato: ", type(list2))

thisList = list(("manzana", "tetera", "camioneta", "coche")) # note the double round-brackets
print(thisList)

print(thisList[0]) #Imprime el primer elemento
print(thisList[-1]) #Imprime el ultimo elemento
print(thisList[0:2]) #Imrpime desde el primer item all 2 segundo
print(thisList[:3]) #Los tres primeros items
print(thisList[1:]) #Imprime desde el segundo item hasta el final
print(thisList[-3:-1]) #Imrpime desde el final, sin incluir el último item

if "tetera" in thisList:
    print("tetera está dentro de la lista")

#Modificar elementos de una lista
thisList[1]= "Batman"
print(thisList)

thisList[2:3] = ["Superman", "Flash"]
print(thisList)

thisList[1:4] =["Joker"]
print(thisList)

#Añade un elemento o cambialo por otro
thisList.insert(3, "Pingüino")
print(thisList)

#Elimina un elemento
thisList.remove("Joker")
print("Se borra el elemento item", thisList)

#Eliminar un elemento especifico segun su indice
thisList.pop(1)
print("Se borra el elemnto segundo", thisList)

#Eliminar el último elemento
thisList.pop()
print("Se borra el elemento último", thisList)

#Borrar un elemento
del thisList[0]
print("Se borra el primer elemento", thisList)

#Añade un elemento al final de la lista
thisList.append("dragón")
print(thisList)

#Añadir los elemento de una lista a otra
otraLista = ["Rodolfo", "Kike", "Katya", "Dahlia"]
thisList.extend(otraLista)
print(thisList)

#Tambien se puede añadir elementos de cualquier elemento iterable, como por ejemplo una tupla
thisTuple = ("Marbella", "Forasteros")
thisList.extend(thisTuple)
print(thisList)

#Vaciar lista
otraLista.clear()
print("Se vacia la lista", otraLista)

#Borrar una lista
del otraLista
#print(otraLista)

#Loops
for x in thisList:
    print(x)

for i in range(len(thisList)):
    print("Elemento", i + 1, thisList[i])

i = 0
while i < len(thisList):
    print(i +1, thisList[i])
    i += 1

j = 0
[print(x) for x in thisList]

#Añadir elementos a una nueva lista que tengan "a"
nuevaLista = []
for x in thisList:
    if "a" in x:
        nuevaLista.append(x)
print(nuevaLista)

#Otra forma
newList = [x for x in thisList if "f" in x]
print(newList)

#Mostrar item que no son
newList = [x for x in thisList if x != "Rodolfo"]
print(newList)

nuevaLista = [x for x in newList]
print(newList)

#Rango
numLista = [x for x in range(10)] 
print(numLista)

numLista = [x for x in range(10) if x < 5]
print(numLista)

#Poner en mayusculas
nuevaLista = [x.upper() for x in newList]
print(nuevaLista)

#Cambiar elementos de la lista por una palabra
saludoLista = ["hola" for x in newList]
print(saludoLista)

#Cambiar un valor por otro
nuevaLista = [x if x != "dragón" else "Fedor" for x in newList]
print(nuevaLista)

#Ordenar listas ascendente
frutas = ["naranja", "mango", "kiwi", "piña", "frambuesa"]
print(frutas)
frutas.sort()
print(frutas)

#La funcion sort() es sensible a las mayusculasy las coloca antes que la sminusculas
frutas2 = ["Naranja", "mango","apetinas", "kiwi", "piña", "frambuesa"]
frutas2.sort()
print("Con sort() las mayusculas se ordenan antes que las minusculas ", frutas2)
frutas2.sort(key = str.lower)
print("Con sort(key = str.lower se ordenan ignorando las mayusculas", frutas2)

#Ordenar listas descendente
numeros = [100, 20, 33, 44, 5]
numeros.sort(reverse = True)
print(numeros)

#Ordenar una lista dependiendo de lo cerca que ese numero este de otro
def funcion(n):
    return abs(n - 50)

numeros.sort(key = funcion, reverse = True)
print("Orden segun funcion y reverse = True", numeros)

#Mostrar lista desde el final
print("Sin .reverse", numeros)
numeros.reverse()
print("Con .reverse", numeros)

#Copiar lista
ejemplo = ["hola", "mundo", "cruel"]
copia = ejemplo.copy()
print(copia)

copia2 = list(ejemplo)
print(copia2)

#Concatenar listas
lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]

lista3 = lista1 + lista2
print(lista3)

for x in lista2:
    lista1.append(x)
print(lista1)

list1 = ["a", "b" , "c"]

list1.extend(lista2)
print(list1) 

list2 = ["a", "B" , "c"]
list2.sort()
print("La lista se ordena según el código ASCII",list2)

list2.sort(key=str.lower)
print("Con key=str.lower ignoramos las mayusculas a la hora de ordenar una lista", list2)

#https://www.w3schools.com/python/python_lists_methods.asp