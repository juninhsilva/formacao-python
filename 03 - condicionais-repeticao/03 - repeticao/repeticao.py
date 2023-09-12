a = int(input("Informe um número inteiro: "))
print(a) 

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

print(list(range(4)))
print(list(range(0,144)))

for numero in range(0, 51, 5):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")

numero = 1000
print()

while numero > 0:
    print(numero)
    numero-=10
else:
    print("Acabou")