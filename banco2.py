opcao = -1
saldo = 0
depositos = []
saques = []
limite_saque = 0
limite_maximo_saque = 3

while opcao != 0:
    print(
        """
[1] Sacar
[2] Depósito
[3] Extrato
[0] Sair
        """
    )
    opcao = int(input("Digite qual operação você deseja fazer:"))

    if opcao == 1:
        if limite_saque >= limite_maximo_saque:
            print("Limite diário de saques atingido!")
        else:
            valor_saque = int(input("Qual o valor do saque? "))
            if valor_saque > 500:
                print("O limite máximo para saque é de R$ 500,00")
            elif valor_saque > saldo:
                print("Saldo insuficiente para retirada!")
            else:
                print("Saque retirado!")
                limite_saque += 1
                saques.append(valor_saque)
                saldo -= valor_saque
    elif opcao == 2:
        valor_deposito = int(input("Qual o valor do depósito? "))
        depositos.append(valor_deposito)
        saldo += valor_deposito
        print("Depósito concluído!")
    elif opcao == 3:
        print(f"""
=====SALDO=====
R$ {saldo:.2f}

===============

=====SAQUES====
{', '.join([f'R$ {saque:.2f}' for saque in saques])}

===============

===DEPÓSITOS===
{', '.join([f'R$ {deposito:.2f}' for deposito in depositos])}

Limite de saques restante: {limite_maximo_saque - limite_saque}
        """)
    elif opcao == 0:
        print("Saindo...")
    else:
        print("Opção inválida!")
