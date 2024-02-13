import random
import tkinter as tk
import pygame

def adivinhe_o_numero():
    pygame.mixer.init()
    som_fogos = pygame.mixer.Sound("fogos.wav")
    som_fogos.set_volume(0.5)

    numero_secreto = random.randint(1,100)
    tentativas = 0

    # Função para verificar palpite
    def verificar_palpite(event=None):
        nonlocal tentativas
        palpite = int(entrada.get())
        tentativas += 1

        if palpite < numero_secreto:
            resultado.config(text="Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            resultado.config(text="Muito alto! Tente um número menor.")
        else:
            resultado.config(text=f"Muito bem!!! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas. Você é de mais.")
            som_fogos.play()

    # Configuração da janela
    janela = tk.Tk()
    janela.title("Adivinhe o número!")
    janela.geometry("500x200")

    # Elementos da janela
    label = tk.Label(janela, text="Digite seu palpite:")
    label.pack()

    entrada = tk.Entry(janela)
    entrada.pack()
    entrada.bind("<Return>", verificar_palpite)

    botao = tk.Button(janela, text="Verificar", command=verificar_palpite)
    botao.pack()

    resultado = tk.Label(janela, text="")
    resultado.pack()

    janela.mainloop()

adivinhe_o_numero()

#feito pelo daniel l. b. da silva
