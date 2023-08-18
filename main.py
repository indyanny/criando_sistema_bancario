menu = ("Menu")

[1] Saque 
[2] Extrato
[3] Deposito
[0] Sair

=> ---

saldo = 0
limite = 1500
extrato = "extrato"
numero_saques = 3
LIMITE_SAQUE = 1500

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor de saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques = LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente!")

        elif excedeu_limite:
            print("Operação falhou! Limite excedido!")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques foi excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "2":
        print("\n==============EXTRATO==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {valor: .2f}")
        print("======================================")

    elif opcao == "3":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")