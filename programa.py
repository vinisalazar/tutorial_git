def main(a, b):
    """
	Esse é a função principal do nosso programa.
	A e B devem ser números.
	Retorna a soma.
	"""
    result = round(a ** b, 2)
    print(f"\nO resultado é {result}")


def validate(x):
    """
	Função de validação do input.
	"""
    try:
        val = float(x)
        return val
    except ValueError:
        print("Esse valor não é válido! Use um número.\n")
        return None


if __name__ == "__main__":
    print("Bem vindo ao nosso programa de soma!\n")
    a = input("Digite seu primeiro número.\n")
    while validate(a) == None:
        a = input("Digite seu primeiro número.\n")

    b = input("\nDigite seu segundo número.\n")
    while validate(b) == None:
        b = input("Digite seu segundo número.\n")

    main(float(a), float(b))
