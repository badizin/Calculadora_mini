def divisao():
    try:
        a1 = float(input("Digite o primeiro número: "))
        a2 = float(input("Digite o segundo número: "))
        resultado = a1/a2
        print(f"O resultado da divisão é: {resultado}")
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

divisao()