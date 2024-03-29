
def selecionar_equacao( n1, operador, n2 ):
    if operador == '+':
        return n1+n2

    elif operador == '-':
        return n1 - n2

    elif operador == '*':
        return n1 * n2

    elif operador == '/':
        if n2 != 0:

            return n1 / n2

        else:

            return "Erro: divisão por 0"

    else:

        return "operador invalido!"


n1 = int(input("digite um numero: "))

operacao = input("qual operação voce pretende fazer? (+, -, *, /): ")

n2= int(input("digite um numero: "))

resultado = (selecionar_equacao(n1, operacao, n2))

print("o resultado de: ", n1, operacao, n2, "é ", resultado )

print("Codigo criado por Daniel Luis")