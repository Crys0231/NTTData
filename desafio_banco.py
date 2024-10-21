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

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print("Depósito realizado.")
        else:  
            print("Valor informado não é positivo")
             

    elif opcao == "s":
        print("Saque") 

        valor = float(input("Digite o valor à tirar: "))
        maior_que_saldo = valor > saldo
        maior_que_limite = valor > limite
        limite_saque = numero_saques >= LIMITE_SAQUES

        if maior_que_saldo:
            print("Valor maior que o saldo atual.")
        elif maior_que_limite: 
            print("Número não está dentro do limite de R$500,00.")
        elif limite_saque:
            print("Número de saques excedido.")
        elif valor > 0: 
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado.")
        else: 
            print("Operação falhou")
            

    elif opcao == "e": 
        print("Extrato")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo em conta: R$ {saldo:.2f}.")
        

    elif opcao == "q":
        break
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada")
        
