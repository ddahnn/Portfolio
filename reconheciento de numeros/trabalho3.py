
def lista_par(numero, listaPar):
  if numero % 2 == 0:
    listaPar.append(numero)
    print("numero adicionado a lista Par!")


def lista_impar(numero, listaImpar):
  if numero %2 != 0:
    listaImpar.append(numero)
    print("numero adicionado a lista Impar!")


def multiplos_de_5(numero, listaMultiplos):
  if numero % 5 == 0:
    listaMultiplos.append(numero)
    print("Número adicionado a lista Multiplos de 5!")

def limpar_listas(lista_g):
  if len(lista_g) == 10:
    lista_g.clear()
    print("Lista limpa!")

def numeros_permitidos(numero):
  if numero <= 0 or numero > 1000:
    print("Digite apenas numero entre 1 e 1000")
    return False
  return True
  

def imprimir_listas(lista_g, nome_lista):
  print(f"Lista {nome_lista}:")
  for i, item in enumerate(lista_g):
    print(f" {i} - {item}")


def main():
  listaPar, listaImpar, listaMultiplos5 = [], [], []
  
  contador = 0
  
  while contador < 30:
    numero = int(input(f"\nDigite um numero intero entre 1 e 1000 (para encerrar digite 999): "))
    if numero == 999:
      break
      
    if not numeros_permitidos(numero):
      continue
    contador += 1
    lista_par(numero, listaPar)
    lista_impar(numero, listaImpar)
    multiplos_de_5(numero, listaMultiplos5)
    
    limpar_listas(listaPar)
    limpar_listas(listaImpar)
    limpar_listas(listaMultiplos5)
   
    
      
  imprimir_listas(listaPar, "Lista Par")
  imprimir_listas(listaImpar, "Lista Impar")
  imprimir_listas(listaMultiplos5, "Lista multiplos de 5")
      
if __name__ == "__main__":
  main()

'''
Código feito por Daniel luis
e-mail para contato: ddahnn@gmail.com
'''