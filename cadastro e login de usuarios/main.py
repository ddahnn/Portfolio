import tkinter as tk
from tkinter import messagebox
import json


def salvar_usuarios():
  usuario = {
    "nome" : entry_nome.get(),
    "Genero" : entry_genero.get(),
    "email" : entry_email.get(),
    "telefone" : entry_telefone.get(),
    "endereço" : entry_endereco.get(),
    "usuario" : entry_usuario.get(),
    "Senha" : entry_senha.get()
  }
  with open('usuarios.json', "a") as arquivo:
    json.dump(usuario, arquivo)
    arquivo.write('\n')
  messagebox.showinfo("sucesso", "Usuário salvo com sucesso")

janela_cadastro = tk.Tk()
janela_cadastro.title("Cadastro de Usuários")

'''criação dos campos de entrada'''
tk.Label(janela_cadastro, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(janela_cadastro)
entry_nome.grid(row=0, column=1)

tk.Label(janela_cadastro, text="Gênero").grid(row=1, column=0)
entry_genero = tk.Entry(janela_cadastro)
entry_genero.grid(row=1, column=1)

tk.Label(janela_cadastro, text="Email").grid(row=2, column=0)
entry_email = tk.Entry(janela_cadastro)
entry_email.grid(row=2, column=1)

tk.Label(janela_cadastro, text="Telefone").grid(row=3, column=0)
entry_telefone = tk.Entry(janela_cadastro)
entry_telefone.grid(row=3, column=1)

tk.Label(janela_cadastro, text="Endereço").grid(row=4, column=0)
entry_endereco = tk.Entry(janela_cadastro)
entry_endereco.grid(row=4, column=1)

tk.Label(janela_cadastro, text="Usuário").grid(row=5, column=0)
entry_usuario = tk.Entry(janela_cadastro)
entry_usuario.grid(row=5, column=1)

tk.Label(janela_cadastro, text="Senha").grid(row=6, column=0)
entry_senha = tk.Entry(janela_cadastro, show="*")
entry_senha.grid(row=6, column=1)

#botão para salvar os dados
botao_salvar = tk.Button(janela_cadastro, text='Salvar', command=salvar_usuarios)
botao_salvar.grid(row=7, column=0, columnspan=2)

janela_cadastro.mainloop()