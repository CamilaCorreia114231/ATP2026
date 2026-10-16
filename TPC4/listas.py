import random
 
def criar_lista():
    n = int(input("Quantos elementos? "))
    res = []
    while n > 0:
        num = random.randint(1, 100)
        res.append (num)
        n = n - 1
    return res 

def ler_lista(N):
    res = []
    while N > 0:
        i = int(input("Introduz um número"))
        res.append (i)
        N = N - 1
    return res

def somar_lista(lista):
    res = 0
    for n in lista:
        res = res + n
    return res

def media_lista(lista):
    res = 0
    for n in lista:
        res = res + n
        x = res/ len(lista)
    return x

def maior_lista(lista):
    res = lista [0]
    for n in lista:
        if n > res:
            res = n
    return res

def menor_lista(lista):
    res = lista [0]
    for n in lista:
        if n < res:
            res = n
    return res

def ordlista_cresc(lista):
    i = 0
    res = True
    while i < len(lista) - 1 and res:
        if lista[i] > lista[i + 1]:
            res = False
        i = i + 1
    return res

def ordlista_decresc(lista):
    i = 0
    res = True
    while i < len(lista) - 1 and res:
        if lista[i] < lista[i + 1]:
            res = False
        i = i + 1
    return res

def proc_elem(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

    return -1
        
def sair_lista():
    print ("Lista final:", lista)



lista = []
opcao = ""

while opcao != 0:
    print("MENU")
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        lista = criar_lista()
        print(lista)

    elif opcao == 2:
        n = int(input("Quantos elementos? "))
        lista = ler_lista(n)
        print(lista)

    elif opcao == 3:
        print("Soma =", somar_lista(lista))

    elif opcao == 4:
        if len(lista) == 0:
            print ("Não existe lista.")
        else:
            print("Média =", media_lista(lista))

    elif opcao == 5:
        if len(lista) == 0:
            print ("Não existe lista.")
        else:
            print("Maior =", maior_lista(lista))

    elif opcao == 6:
        if len(lista) == 0:
            print ("Não existe lista.")
        else:
            print("Menor =", menor_lista(lista))

    elif opcao == 7:
        if ordlista_cresc(lista):
            print("Sim")
        else:
            print("Não")

    elif opcao == 8:
        if ordlista_decresc(lista):
            print("Sim")
        else:
            print("Não")

    elif opcao == 9:
        elem = int(input("Elemento a procurar: "))
        print(proc_elem(lista, elem))

    elif opcao == 0:
        print("Lista final:", lista)

    else:
        print("Opção inválida!")