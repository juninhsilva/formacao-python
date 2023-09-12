menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Limites
    [q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        print("Depósitos")
        valor = float(input("Digite o valor do Depósito: "))

        if(valor > 0):

            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido.")
    
    elif opcao == "s":
        
        print("Saques")
        
        if(saldo > 0 and LIMITE_SAQUES > numero_saques):
            valor = float(input("Digite o valor do Saque: "))
            
            if(saldo >= valor and valor <= limite):
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
           
            else:
                print("Não foi possível realizar a operação.\nVerifique seu saldo e limite de saques.")
        
        else:
            print("Não foi possível realizar a operação.\nVerifique seu saldo e limite de saques.")
    
    elif opcao == "e":
        print(" ---------- Extrato ---------- ")
        print("Não foram realizadas transações." if not extrato else extrato)
        print(extrato)
        print(f"Saldo: R$: {saldo:.2f}")
        print(" ----------------------------- ")

    elif opcao == "l":
        print(" ---------- Limites ---------- ")
        print("Não foram realizadas transações.\n" if not extrato else extrato)
        print(f"Limite de Saques: {LIMITE_SAQUES}")
        print(f"Saques já realizados: {numero_saques}")
        print(" ----------------------------- ")

    
    elif opcao == "q":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!\n Selecione uma operação dentre as disponíveis.")

