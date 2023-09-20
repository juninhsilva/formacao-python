frutas = []
print(frutas)
frutas = ["laranja", "banana", "maçã", "uva"]
print(frutas)

letras = list("python")
print(letras)
print(letras[2:])
print(letras[:2])
print(letras[0:3])
print(letras[0:4:2])
print(letras[::])
print(letras[::-1])

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "458 Italia", 4200000, 2023, 2932, "Alpinópolis", "MG", True]
print(carro)

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [5, "c", 6],
]
print(matriz)
print(matriz[1])
print(matriz[0][1])

matriz.append([7,8,"d"])
print(matriz)

lista = []

lista.append(1)
lista.append("Python")

print(lista)

lista.clear()
print(lista)

lista = [1, 2, 3, 4, 5]
lista2 = lista.copy()

print(id(lista), id(lista2))

print(lista2.count(1))
print(lista2.count(2))
print(lista2.count(3))

lista.extend(lista2)

print(lista)

print(lista.index(3))

lista.pop(2)
print(lista)

lista.remove(5)
print(lista)

lista.reverse()
print(lista)

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista = ["111", "2", "30", "55463", "41", "747", "95", "8", "6"]
lista.sort(key=lambda x: len(x))
print(lista)

lista.sort(key=lambda x: len(x), reverse=True)
print(lista)