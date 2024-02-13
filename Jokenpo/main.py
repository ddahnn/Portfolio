import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Certifique-se de ter o módulo Pillow instalado: pip install Pillow

def jogo_pedra_papel_tesoura(escolha_usuario):
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)

    resultado = ''
    if escolha_usuario == escolha_computador:
        resultado = 'Empate!'
    elif (
        (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or
        (escolha_usuario == 'papel' and escolha_computador == 'pedra') or
        (escolha_usuario == 'tesoura' and escolha_computador == 'papel')
    ):
        resultado = 'Você ganhou!'
    else:
        resultado = 'Você perdeu!'

    messagebox.showinfo('Resultado', f'Você escolheu: {escolha_usuario}\nComputador escolheu: {escolha_computador}\n\n{resultado}')

def escolher_objeto(objeto):
    jogo_pedra_papel_tesoura(objeto)

# Configuração da janela
janela = tk.Tk()
janela.title('Jogo Pedra, Papel e Tesoura')

# Carregando imagens
imagem_pedra = ImageTk.PhotoImage(Image.open("pedra.png"))
imagem_papel = ImageTk.PhotoImage(Image.open("papel.png"))
imagem_tesoura = ImageTk.PhotoImage(Image.open("tesoura.png"))

# Criando botões de imagem
botao_pedra = tk.Button(janela, image=imagem_pedra, command=lambda: escolher_objeto('pedra'))
botao_papel = tk.Button(janela, image=imagem_papel, command=lambda: escolher_objeto('papel'))
botao_tesoura = tk.Button(janela, image=imagem_tesoura, command=lambda: escolher_objeto('tesoura'))

# Posicionando botões na janela
botao_pedra.pack(side=tk.LEFT, padx=10)
botao_papel.pack(side=tk.LEFT, padx=10)
botao_tesoura.pack(side=tk.LEFT, padx=10)

# Iniciando o loop da interface gráfica
janela.mainloop()
