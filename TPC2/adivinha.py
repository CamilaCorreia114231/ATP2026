### Jogo Adivinha o Numero

def util_adv():
    import random
    num = random.randint(0, 100)
    tent = 0
    palp = 0

    while palp != num:
        tent = tent + 1
        palp = int(input("Qual é o teu palpite?"))

        if palp == num:
            print (f"Acertaste! Em apenas {tent} tentativas!")
        elif palp < num:
            print ("O número que eu pensei é maior!")
        else:
            print ("O número que eu pensei é menor!")



def comp_adv():
    print ("Escolhe um número, de 0 a 100. Apenas podes responder com: Acertaste; Menor; Maior.")

    min = 0
    max = 100
    tent = 0
    feedback = 0

    while feedback != "Acertaste":
        palp = (min + max) // 2
        tent = tent + 1
        feedback = input(f"O meu palpite é {palp}")

        if feedback == "Acertaste" :
            print (f"Acertei com apenas com {tent} tentativas!")
        elif feedback == "Menor" :
            max = palp - 1
        elif feedback == "Maior" :
            min = palp + 1 




print ("Vamos jogar um jogo: Adivinha o número! Qual das opções queres jogar?")
print ("Opção 1 - Eu escolho um número e tu adivinhas.")
print ("Opção 2 - Tu escolhes um número e eu adivinho.")

opçao = input ("Escolhe uma opção:")
if opçao == "1":
    util_adv()
elif opçao == "2":
    comp_adv()