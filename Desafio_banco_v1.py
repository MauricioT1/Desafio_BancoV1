menu = """
Escolha uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

-> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"""Depósito: \t \t R$ {valor:.2f}\n------------------------------------------\n"""

        else:
            print("O valor informado é inválido, Tente novamente.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("O valor do saque excede o limite!")

        elif excedeu_saques:
            print("Número máximo de saques excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"""Saque: \t \t \t R$ {valor:.2f}\n------------------------------------------\n"""
            numero_saques += 1

        else:
            print("O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("==========================================")
        print(f"Saldo: \t \t \t  R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print( "Obrigado por usar nosso caixa eletrônico!\n" )
        break 

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")