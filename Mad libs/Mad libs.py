import tkinter as tk
from tkinter import messagebox
import json

def preencher_historia(substantivo, verbo, adjetivo, lugar, nome_proprio, adverbio):
    return f"Num belo {adjetivo} dia, {nome_proprio} decidiu {verbo} um {substantivo} em {lugar}. Surpreendentemente, ele o fez {adverbio}."

# Função para atualizar a interface
def atualizar_interface():
    grupo_atual = grupos_palavras[grupo_index[0]]
    label_palavra.config(text=f"{grupo_atual.capitalize()}:")
    entry_palavra.delete(0, tk.END)  # Limpar o campo de entrada

# Função para obter palavras
def obter_palavra(event=None):
    palavra = entry_palavra.get()
    palavras[grupos_palavras[grupo_index[0]]] = palavra
    entry_palavra.delete(0, tk.END)  # Limpar o campo de entrada

    # Armazenar palavra aprendida no dicionário de palavras
    palavra_aprendida = palavras_aprendidas.get(grupos_palavras[grupo_index[0]], [])
    palavra_aprendida.append(palavra)
    palavras_aprendidas[grupos_palavras[grupo_index[0]]] = palavra_aprendida

    # Avançar para o próximo grupo ou exibir a história se todos os grupos foram preenchidos
    grupo_index[0] += 1
    if grupo_index[0] < len(grupos_palavras):
        atualizar_interface()
    else:
        historia_mad_libs = preencher_historia(*palavras.values())
        label_resultado.config(text=historia_mad_libs)

# Função para oferecer sugestões
def oferecer_sugestoes():
    grupo_atual = grupos_palavras[grupo_index[0]]
    palavras_aprendidas_grupo = palavras_aprendidas.get(grupo_atual, [])
    if palavras_aprendidas_grupo:
        sugestoes = ", ".join(palavras_aprendidas_grupo)
        messagebox.showinfo("Sugestões", f"Sugestões para {grupo_atual.capitalize()}: {sugestoes}")
    else:
        messagebox.showinfo("Sugestões", f"Nenhuma sugestão disponível para {grupo_atual.capitalize()}.")

# Função para reiniciar o jogo
def reiniciar_jogo():
    # Limpar variáveis e atualizar a interface
    global grupo_index, palavras
    grupo_index = [0]
    palavras = {}
    atualizar_interface()

# Função para salvar palavras aprendidas em um arquivo JSON
def salvar_palavras_aprendidas():
    with open('palavras_aprendidas.json', 'w') as arquivo:
        json.dump(palavras_aprendidas, arquivo)
    messagebox.showinfo("Salvo", "Palavras aprendidas salvas com sucesso!")

# Função para carregar palavras aprendidas de um arquivo JSON
def carregar_palavras_aprendidas():
    try:
        with open('palavras_aprendidas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

# Função a ser chamada ao fechar a janela
def fechar_janela():
    salvar_palavras_aprendidas()
    janela.destroy()

# Criar janela
janela = tk.Tk()
janela.title("Mad Libs Python")
janela.geometry("400x300")  # Definir tamanho da janela

# Definir grupos de palavras
grupos_palavras = ['substantivo', 'verbo', 'adjetivo', 'lugar', 'nome proprio', 'adverbio']

# Inicializar variáveis
grupo_index = [0]
palavras = {}
palavras_aprendidas = carregar_palavras_aprendidas()

# Criar rótulo e entrada de texto
label_palavra = tk.Label(janela, text=f"{grupos_palavras[grupo_index[0]].capitalize()}:")
label_palavra.grid(row=0, column=0, pady=(50, 0), padx=10)  # Adicionar espaçamento vertical (pady) e horizontal (padx)

entry_palavra = tk.Entry(janela, width=20)
entry_palavra.grid(row=0, column=1, pady=(50, 0), padx=10)  # Adicionar espaçamento vertical (pady) e horizontal (padx)

# Botão para obter palavra
btn_obter_palavra = tk.Button(janela, text="Enviar", command=obter_palavra)
btn_obter_palavra.grid(row=0, column=2, pady=(50, 0), padx=10)  # Adicionar espaçamento vertical (pady) e horizontal (padx)

# Botão para oferecer sugestões
btn_sugestoes = tk.Button(janela, text="Sugestões", command=oferecer_sugestoes)
btn_sugestoes.grid(row=1, column=0, columnspan=3, pady=10)  # Adicionar espaçamento vertical (pady)

# Botão para reiniciar o jogo
btn_reiniciar_jogo = tk.Button(janela, text="Reiniciar Jogo", command=reiniciar_jogo)
btn_reiniciar_jogo.grid(row=2, column=0, columnspan=3, pady=10)  # Adicionar espaçamento vertical (pady)

# Label para exibir o resultado
label_resultado = tk.Label(janela, text="Sua história aparecerá aqui!")
label_resultado.grid(row=3, column=0, columnspan=3, pady=10)  # Adicionar espaçamento vertical (pady)

# Configurar o evento ao fechar a janela
janela.protocol("WM_DELETE_WINDOW", fechar_janela)

# Atualizar a interface inicial
atualizar_interface()

# Configurar o evento Enter para obter palavra
janela.bind("<Return>", obter_palavra)

# Centralizar a janela
largura_janela = janela.winfo_reqwidth()
altura_janela = janela.winfo_reqheight()
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = int((largura_tela / 2) - (largura_janela / 2))
pos_y = int((altura_tela / 2) - (altura_janela / 2))
janela.geometry(f"+{pos_x}+{pos_y}")

# Iniciar a janela
janela.mainloop()

#criado por daniel
