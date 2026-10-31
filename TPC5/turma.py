def criar_turma():
    return []

def inserir_aluno(turma):
    nome = input("Qual o nome da aluna/o? ")
    id = int(input("Qual o ID da aluna/o? "))
    notatpc = int(input("Qual a nota do TPC? "))
    notaproj = int(input("Qual a nota do projeto? "))
    notateste = int(input("Qual a nota do teste? "))

    aluno = (nome, id, [notatpc, notaproj, notateste])
    turma.append(aluno)

def lista_turma(turma):
    for aluno in turma:
        print (aluno)

def consu_aluno(turma, proc_id):
    for aluno in turma:
        if aluno[1] == proc_id:
            return aluno
        
    return None


def guardarTurma(turma):
    ficheiro = open("turma.txt", "w")

    for aluno in turma:
        ficheiro.write(str(aluno) + "\n")

    ficheiro.close()

    print("Turma guardada com sucesso!")

def carregarTurma():
    turma = []

    ficheiro = open("turma.txt", "r")

    for linha in ficheiro:
        aluno = eval(linha)
        turma.append(aluno)

    ficheiro.close()

    print("Turma carregada com sucesso!")
    return turma


turma = []
opcao = ""

while opcao != 0:
    print("Menu")
    print ("Opção 1: Criar uma turma.")
    print ("Opção 2: Inserir um aluno na turma.")
    print ("Opção 3: Listar a turma.")
    print ("Opção 4: Consultar um aluno por id.")
    print ("Opção 8: Guardar a turma em ficheiro.")
    print ("Opção 9: Carregar uma turma dum ficheiro.")
    print ("Opção 0: Sair da aplicação.")
    opcao = int (input("Opção: "))

    if opcao == 1:
        turma = criar_turma()
      
    elif opcao == 2:
        inserir_aluno(turma)
      
    elif opcao == 3:
        lista_turma(turma)
      
    elif opcao == 4:
        proc_id = int(input("ID do aluno: "))
        aluno = consu_aluno(turma, proc_id)

        if aluno == None:
            print("Aluno não encontrado")
        else:
            print(aluno)

    elif opcao == 8:
        guardarTurma(turma)

    elif opcao == 9:
        turma = carregarTurma()

    elif opcao == 0:
        print("Aplicação terminada.")

    else:
        print("Opção inválida.")