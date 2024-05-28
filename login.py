import tkinter as tk
from tkinter import messagebox
import json

def verificar_login():
    email = entry_email_login.get()
    senha = entry_senha_login.get()

    try:
        with open('usuarios.json', 'r') as arquivo:
            for linha in arquivo:
                usuario = json.loads(linha)
                if usuario['email'] == email and usuario['Senha'] == senha:
                    messagebox.showinfo("Sucesso", "Login realizado com sucesso.")
                    return
            messagebox.showerror("Erro", "Email ou senha incorretos.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "nenhum usuario foi encontrado.")

#configuração da janela de login
janela_login = tk.Tk()
janela_login.title("login")

tk.Label(janela_login, text="Email").grid(row=0, column=0)
entry_email_login = tk.Entry(janela_login)
entry_email_login.grid(row=0, column=1)

tk.Label(janela_login, text="Senha").grid(row=1, column=0)
entry_senha_login = tk.Entry(janela_login)
entry_senha_login.grid(row=1, column=1)

botão_login = tk.Button(janela_login, text="Login", command=verificar_login)
botão_login.grid(row=2, column=0, columnspan=2)

janela_login.mainloop()


'''Feito por Daniel Luis'''
'''Contato e-mail  ddahnn@gmail.com'''