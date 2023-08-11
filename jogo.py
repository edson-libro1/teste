import random

print("bem vindo a o jogo de adivinhação!")
numero_secreto = random.randint(1,100)
totaldetentativa = 3
for rodada in range(1, totaldetentativa +1 ):    

     print("Tentativa {} de {}".format(rodada, totaldetentativa))
     chute = int(input("digite um número entre 1 e 100"))
     print("você digitou: ", chute) 
     
     acertou = chute == numero_secreto

     maior = chute > numero_secreto
     menor = chute < numero_secreto

     if (acertou):
        print("você acertou!")
        break
     else:
       if (maior):
            print("você errou! O seu chute foi maior que número secreto.")
       elif(menor):
            print("você errou! O seu chute foi menor que o número secreto.")

            print("fim do jogo")
        