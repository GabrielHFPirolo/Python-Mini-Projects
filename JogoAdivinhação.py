from random import randint
quantidadeTentativas = 1
numeroSorteado = randint(1, 100)
try:
  print("Tente Adivinhar qual número estou pensando!")
  tentativa = int(input("Diga sua tentativa de 1 a 100: "))
  while tentativa < 1:
    print("Jogue apenas valores a partir de 1")
    tentativa = int(input("Tente novamente:"))
  def jogabilidade():
    if tentativa > numeroSorteado:
      print("Tente um número menor")
    else:
      print("Tente um número maior")

  while tentativa != numeroSorteado:
    quantidadeTentativas += 1
    jogabilidade()
    tentativa = int(input("Digite aqui a nova tentativa: "))
  print(f"Parabéns! você ganhou em {quantidadeTentativas} tentativas!")
except ValueError:
  print("Você digitou um valor inválido...")
except:
  print("Algo deu errado...")
