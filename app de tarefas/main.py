def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar tarefas")
    print("2. Listar tarefas")
    print("3. Remover tarefas")
    print("4. Sair")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicada com sucesso!")

def listar_tarefas(tarefas):
    print('\nTarefas: ')
    for i,tarefa in enumerate(tarefas, 1):
        print(f'{i}. {tarefa}')

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    num_tarefas = int(input("\nDigite o número da tarefa a ser removida: "))
    if 1<= num_tarefas <= len(tarefas):
        tarefa_removida = tarefas.pop(num_tarefas - 1)
        print(f"tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Número Invalido!")


def main():
    tarefas = []
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            remover_tarefa(tarefas)
        elif escolha == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção invalida! Tente novamente")

if __name__ == "__main__":
    main()