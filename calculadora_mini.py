def somar():
    print('somado!')
def subtrair():
    print('somado!')
def multiplicar():
    print('somado!')
def divir():
    print('somado!')




while True:
    print(' Bem Vindo a calculadora BUSINESS TECH FUCAPE!')
    E1 = input("\n\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Sair")
    if E1 == '1':
        somar()
    elif E1 == '2':
        subtrair()
    elif E1 == '3':
        multiplicar()
    elif E1 == '4':
        divir()
    elif E1 == '5':
        print('Saindo')
        break
    else: print("Selecione uma opção válida")
