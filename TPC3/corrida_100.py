### Corrida para os 100

import random

def util_start():
    total = 0
    jogada = 0
    comp = 0
    ha_vencedor = False 

    while total < 100 and not ha_vencedor:
        jogada= int (input("Qual o valor da tua jogada?"))

        while jogada < 1 or jogada > 10 or (total + jogada) > 100:
            print ("Jogada inválida! Relembro a tua jogada apenas pode ir do 1 ao 10!")
            jogada= int (input(f"Valor atual: {total}. Qual o valor da tua jogada?"))

        total = total + jogada

        if total == 100:
            print ("Chegaste aos 100! Parabéns!")
            ha_vencedor = True
        elif 100 - total <= 10:
            comp = 100 - total 
            total = total + comp
            print (f"Valor da minha jogada: {comp}. Atingi os 100! Ganhei!")
            ha_vencedor = True
        else:
            comp = 11- jogada   
            total = total + comp
            print (f"Valor da minha jogada: {comp}. Valor atual: {total}")
            if total == 100:
                print("Atingi os 100! Ganhei!")
                ha_vencedor = True





def comp_start():
    total = 0
    comp = 1
    total = total + comp
    print (f"Valor da minha jogada: {comp}.Valor atual: {total}.")
    ha_vencedor = False
   
    while total < 100 and not ha_vencedor:
        jogada= int (input(f"Valor atual: {total}. Qual o valor da tua jogada?"))

        while jogada < 1 or jogada > 10 or (total + jogada) > 100:
            print ("Jogada inválida! Relembro a tua jogada apenas pode ir do 1 ao 10!")
            jogada= int (input(f"Valor atual: {total}. Qual o valor da tua jogada?"))

        total = total + jogada

        if total == 100:
            print ("Chegaste aos 100! Parabéns!")
            ha_vencedor = True
        elif 100 - total <= 10:
            comp = 100 - total 
            total = total + comp
            print (f"Valor da minha jogada: {comp}. Atingi os 100! Ganhei!")
            ha_vencedor = True
        else:
            comp = 11- jogada   
            total = total + comp
            print (f"Valor da minha jogada: {comp}. Valor atual: {total}")
            if total == 100:
                print("Atingi os 100! Ganhei!")
                ha_vencedor = True


        



print ("Vamos jogar um jogo. O objetivo é chegar primeiro aos 100, mas apenas podemos adicionar de 1-10 em cada jogada.")
print ("Queres começar ou eu posso começar?")
print ("Opção 1- O utilizador começa.")
print ("Opção 2- O computador começa.")

opçao = input ("Escolhe uma opção:")
if opçao == "1":
    util_start()
elif opçao == "2":
    comp_start()

