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