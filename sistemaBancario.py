menu = """"

[d] Deposito
[s] Sacar 
[e] Extrato
[q] Sair

"""

saldo = 0 
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Deposito")
        valor = float(input("Digite o valor desejado a depositar: "))
        if valor < 0:
            print("valor inválido")
        else:
            saldo += valor
            extrato += f"Depósitos R${valor:.2f}\n"
    
    elif opcao == "s":
        print("Sacar")
        saque = float(input("digite o valor que deseja sacar: "))
        if LIMITE_SAQUE <= numeros_saques:
            print("Limite de saques já atingido")
        elif saque > limite:
            print("Saque maior qur o permitido")
        elif saque > saldo:
            print("Não possui saldo suficiente")
        else:
            saldo -= saque
            numeros_saques =+ 1
            extrato += f"Saque: R${saque:.2f}\n"
            
            
    
    elif opcao == "e":
        print("Extrato")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo R${saldo:.2f}")
        print("===========================================")
        
    elif opcao == "q":
        print("Sair")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    