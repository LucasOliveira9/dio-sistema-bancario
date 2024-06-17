menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=>
'''

saldo = 0
saques = 0
LIMITE_SAQUES = 3
LIMITE_SAQUE = 500
extrato = ""

while True:
    option = input(menu)

    if(option == 'd'):
        valor = float(input("Valor de Depósito: "))
        saldo+= valor
        extrato+=f"Depósito: R$ {valor:.2f}\n"
    elif(option == 's'):
        valor = float(input("Valor de Saque: "))
        if(valor >= saldo):
            print("Saldo insuficiente")
        elif(valor > LIMITE_SAQUE):
            print("Valor maior que o limite permitido")
        elif(saques >= 3):
            print("Limite de saques diários alcançado")
        else:
            saldo-=valor+0
            saques+=1
            extrato+=f"Saque: R$ {valor:.2f}\n"
    elif(option == 'e'):
        print("\n*****************EXTRATO*****************")
        print("Não Foram Realizadas Movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n*****************************************")
    elif(option == 'x'):
        break
    else:
        print("Opção Inválida")
          
