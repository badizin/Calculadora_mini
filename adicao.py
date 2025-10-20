# Função adição
def adicao(a, b):
    a = float(a)
    b = float(b)
    return a + b


if __name__ == "__main__":
    a = input("Me fale um número: ")
    b = input("Me fale um número: ")
    print(f"O resultado da soma é {adicao(a, b)}")
