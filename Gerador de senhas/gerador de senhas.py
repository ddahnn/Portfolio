import random
import string
import tkinter as tk
import pyperclip

def gerar_senhas(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def copiar_senha():
    senha_gerada = gerar_senhas()
    pyperclip.copy(senha_gerada)
    resultado_label.config(text="senha copiada para a area de transferencia")


def exibir_senha():
    senha_gerada = gerar_senhas()
    resultado_label.config(text="Senha gerada: " + senha_gerada)

#configurar janela
janela = tk.Tk()
janela.title("gerador de senhas" )

#botão para gerar senha
botao_gerar = tk.Button(janela, text="gerar senha", command=exibir_senha)
botao_gerar.pack(pady=10)

#botão copiar

botao_copiar = tk.Button(janela, text="copiar senha", command=copiar_senha)
botao_copiar.pack()

#label para exibir a senha
resultado_label = tk.Label(janela, text='')
resultado_label.pack()

janela.mainloop()




# Testar o gerador de senha
senha_gerada = gerar_senhas()
print("Senha gerada:", senha_gerada)

#%%
#Feito por Daniel
#%%
