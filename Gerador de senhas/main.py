import random
import string

def gerar_senhas(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Testar o gerador de senha
senha_gerada = gerar_senhas()
print("Senha gerada:", senha_gerada)


#%%
