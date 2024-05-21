'''Daniel luis bortolin da silva'''

def main():
    listaA = []
    listaB = []
    listaC = []
    quantidade_digitada = 0

    while True:
        numero = int(input("Digite um número entre 10 e 100 (ou digite 0 para encerrar): "))

        if numero < 0:
            print("Digite apenas números positivos.")
            continue

        if numero == 0 or quantidade_digitada == 20:
            break

        if 20 <= numero <= 40:
            listaA.append(numero)
            print(listaA)
        elif 50 <= numero <= 70:
            listaB.append(numero)
            print(listaB)
        elif 30 <= numero <= 60:
            listaC.append(numero)
            print(listaC)

        quantidade_digitada += 1

        if len(listaA) == 5:
            listaA.clear()
            print("Lista A foi limpa.")

        if len(listaB) == 5:
            listaB.clear()
            print("Lista B foi limpa.")

        if len(listaC) == 5:
            listaC.clear()
            print("Lista C foi limpa.")

    print("Conteúdo das listas:")
    print("Lista A:")
    for i, num in enumerate(listaA):
        print(f"Posição {i}: {num}")

    print("Lista B:")
    for i, num in enumerate(listaB):
        print(f"Posição {i}: {num}")

    print("Lista C:")
    for i, num in enumerate(listaC):
        print(f"Posição {i}: {num}")

if __name__ == "__main__":
    main()
