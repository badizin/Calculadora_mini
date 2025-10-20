def somar():
    print('somado!')

def subtrair():
    print('subtraido!')

def multiplicar():
    x = float(input("Me diga um número: "))
    y = float(input("Me diga outro número: "))
    resultado = x*y
    print(f'Resultado = {resultado}')

def divir():
    print('dividido!')




while True:
    print(' Bem Vindo a calculadora BUSINESS TECH FUCAPE!')
    E1 = input("\n\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Sair\n\nResposta:  ")
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
