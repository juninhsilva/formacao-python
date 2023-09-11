saldo = 2000

opcao = int(input("Informe uma opção: [1] Saque:\n[2] Depósito:\n[3]Extrato:"))

if opcao == 1:
    saque = float(input("Informe o valor do saque: "))

    if saldo > saque:
        print("Realizando saque")
    else:
        print("Saldo insuficiente")

elif opcao == 2:
    valor = float(input("Digite o valor do depósito: "))
    print(f'Saldo: {saldo}')
    
elif opcao == 3:
    print(f'Saldo: {saldo}')

else:
    print("Opção inválida")