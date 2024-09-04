menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
operacao_invalida = "Operação Inválida!"

print("\n==== Bem vindo ao Dio Bank ====\n\n Selecione uma opção do Menu abaixo:")

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito efetuado com sucesso!\n")

        else: 
            print("A operação falhou! O valor informado é inválido.")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        print("\nSaque efetuado com sucesso!\n")

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"{operacao_invalida.center(34, "=")}\n\n Você não tem saldo suficiente.")

        elif excedeu_limite:
            print(f"{operacao_invalida.center(34, "=")}\n\n O valor do saque excede o limite.")
            
        elif excedeu_saques:
            print(f"{operacao_invalida.center(34, "=")}\n\n Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print(f"{operacao_invalida.center(30, "=")}\n\n O valor informado é inválido.")

    elif opcao == "e":

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("\nObrigado por utilizar nosso sistema.\n")
        break
    else:
        print(f"{operacao_invalida.center(37, "=")}\n\n Escolha uma das opções informadas.")