def main():
    lista = []
    while True:
        print("\nQual a opção desejada.")
        print("1 - Adicionar item.")
        print("2 - Remover item.")
        print("3 - Listar itens.")
        print("4 - Sair.")
        selecao = int(input("\nDigite a opção desejada: "))

        if selecao == 1:
            item = input("O que deseja adicionar? ")
            lista.append(item)

        elif selecao == 2:
            for index, item in enumerate(lista):
                print(f"{index} - {item}")
            item_index = int(input("Qual o índice do item que deseja remover? "))
            if 0 <= item_index < len(lista):
                lista.pop(item_index)
                print("\nItem removido com sucesso.")
                
            else:
                print("Índice inválido. Tente novamente.")

        elif selecao == 3:
            for index, item in enumerate(lista):
                print(f"{index} - {item}")

        elif selecao == 4:
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

