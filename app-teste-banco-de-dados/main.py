import sqlite3

def conectar_bd():
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        # Criar tabela de usuários
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, idade INTEGER, email TEXT NOT NULL, telefone TEXT NOT NULL, cidade TEXT NOT NULL)''')
        conn.commit()
        return conn, cursor
    except sqlite3.DatabaseError as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None, None

conn, cursor = conectar_bd()

if not conn:
    print("Não foi possível conectar ao banco de dados.")
else:
    # Função para cadastrar um usuário
    def cadastrar_usuario(nome, idade, email, telefone, cidade):
        cursor.execute('INSERT INTO users (nome, idade, email, telefone, cidade) VALUES (?, ?, ?, ?, ?)', (nome, idade, email, telefone, cidade))
        conn.commit()
        print(f'Usuário {nome} cadastrado com sucesso!')

    # Função para localizar um usuário pelo nome
    def localizar_usuario(nome):
        cursor.execute('SELECT * FROM users WHERE nome = ?', (nome,))
        usuarios = cursor.fetchall()
        if usuarios:
            for usuario in usuarios:
                print(usuario)
        else:
            print(f'Usuário {nome} não encontrado.')

    # Função para atualizar as informações de um usuário
    def atualizar_usuario(id, novo_nome, nova_idade, novo_email, novo_telefone, nova_cidade):
        cursor.execute('UPDATE users SET nome = ?, idade = ?, email = ?, telefone = ?, cidade = ? WHERE id = ?',
                       (novo_nome, nova_idade, novo_email, novo_telefone, nova_cidade, id))
        conn.commit()
        print(f'Usuário com ID {id} atualizado com sucesso!')

    # Função para excluir um usuário
    def excluir_usuario(id):
        cursor.execute('DELETE FROM users WHERE id = ?', (id,))
        conn.commit()
        print(f'Usuário com ID {id} excluído com sucesso!')

    # Função para listar todos os usuários
    def listar_usuarios():
        cursor.execute('SELECT * FROM users')
        usuarios = cursor.fetchall()
        if usuarios:
            for usuario in usuarios:
                print(usuario)
        else:
            print('Nenhum usuário cadastrado.')

    # Menu de operações
    def menu():
        while True:
            print("\nEscolha uma opção:")
            print("1. Cadastrar usuário")
            print("2. Localizar usuário")
            print("3. Atualizar usuário")
            print("4. Excluir usuário")
            print("5. Listar todos os usuários")
            print("6. Sair")

            opcao = input("Digite o número da opção desejada: ")

            if opcao == '1':
                nome = input('Digite seu nome: ')
                idade = input('Digite sua idade: ')
                email = input('Digite seu email: ')
                telefone = input('Digite seu telefone: ')
                cidade = input('Digite sua cidade: ')
                cadastrar_usuario(nome, idade, email, telefone, cidade)

            elif opcao == '2':
                nome = input('Digite o nome do usuário que deseja localizar: ')
                localizar_usuario(nome)

            elif opcao == '3':
                id = input('Digite o ID do usuário que deseja atualizar: ')
                novo_nome = input('Digite o novo nome: ')
                nova_idade = input('Digite a nova idade: ')
                novo_email = input('Digite o novo email: ')
                novo_telefone = input('Digite o novo telefone: ')
                nova_cidade = input('Digite a nova cidade: ')
                atualizar_usuario(id, novo_nome, nova_idade, novo_email, novo_telefone, nova_cidade)

            elif opcao == '4':
                id = input('Digite o ID do usuário que deseja excluir: ')
                excluir_usuario(id)

            elif opcao == '5':
                listar_usuarios()

            elif opcao == '6':
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")

    # Executar o menu
    menu()

    # Fechar a conexão com o banco de dados
    conn.close()
    