import requests
import tkinter as tk
from tkinter import messagebox

def obter_previsao_do_tempo(cidade, chave_api):
    url = f'http://api.weatherapi.com/v1/forecast.json?key={chave_api}&q={cidade}&days=3'
    resposta = requests.get(url)
    dados = resposta.json()

    if 'error' in dados:
        return None, None  # Retorna None se ocorrer um erro

    # Extraindo os dados relevantes
    previsao_atual = dados['current']
    previsao_futura = dados['forecast']['forecastday']
    return previsao_atual, previsao_futura

def buscar_previsao():
    cidade = entrada_cidade.get()
    chave_api = "0bac4f2efa17439091f162811241202"
    previsao_atual, previsao_futura = obter_previsao_do_tempo(cidade, chave_api)

    if previsao_atual and previsao_futura:
        previsao_texto = f"Condição atual: {previsao_atual['condition']['text']}\nTemperatura: {previsao_atual['temp_c']}°C\n\n"
        previsao_texto += "Previsão futura:\n"
        for dia in previsao_futura:
            previsao_texto += f"Dia {dia['date']}: {dia['day']['condition']['text']}\n"
        resultado.configure(text=previsao_texto)
    else:
        messagebox.showerror("Erro", "Erro ao obter a previsão do tempo.")

# Criar janela principal
janela = tk.Tk()
janela.title("Previsão do Tempo")

# Criar widgets
rotulo_cidade = tk.Label(janela, text="Digite o nome da cidade:")
rotulo_cidade.pack()

entrada_cidade = tk.Entry(janela)
entrada_cidade.pack()

botao_buscar = tk.Button(janela, text='Buscar', command=buscar_previsao)
botao_buscar.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

# Iniciar loop de execução
janela.mainloop()
#%%
