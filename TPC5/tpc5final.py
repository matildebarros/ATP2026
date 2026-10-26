

def criar_turma():
    turma = []
    n_alunos = int(input("Quantos alunos quer inserir na turma? "))
    
    for i in range(n_alunos):
        print("Dados do aluno", i + 1, ":")
        nome = input("Nome do aluno: ")
        id = int(input("ID do aluno: "))
        print("Introduz as notas:")
        notaTPC = float(input("Nota TPC: "))
        notaProj = float(input("Nota Projeto: "))
        notaTeste = float(input("Nota Teste: "))

        aluno = (nome, id, [notaTPC, notaProj, notaTeste])
        turma.append(aluno)
    return turma

def inserir_aluno(turma):
    nome = input("Nome do aluno: ")
    id = int(input("ID do aluno: "))

    notaTPC = float(input("Nota TPC: "))
    notaProj = float(input("Nota Projeto: "))
    notaTeste = float(input("Nota Teste: "))

    aluno = (nome, id, [notaTPC, notaProj, notaTeste])
    turma.append(aluno)
    return turma

def listar_turma(turma):
    for aluno in turma:
        nome = aluno[0]
        id = aluno[1]
        notas = aluno[2]
        print("Nome:", nome,"\nID:", id,"\nNotas (TPC, Proj, Teste):", notas)

def consultar_aluno(turma):
    id_procurado = int(input("Introduza o ID do aluno a consultar: "))
    encontrou = 0
    for aluno in turma:
        if aluno[1] == id_procurado:
            print("\nID:", aluno[1], "\nNome:", aluno[0], "\nNotas:", aluno[2])
            encontrou = 1
    if encontrou == 0:
        print("Não foi encontrado nenhum aluno com esse ID")
        


def guardar_turma(turma):
    file = open("turma.txt", "w")
    for aluno in turma:
        nome, id_aluno, notas = aluno
        file.write(f"{nome}|{id_aluno}|")
        for nota in notas:
            file.write(f"{nota};")
        file.write("\n")
    file.close()



def carregar_turma():
    turma = []
    file = open("turma.txt", "r")
    for line in file:
        cada_aluno = line.strip()
        if cada_aluno != "":
            partes = cada_aluno.split("|")
            nome = partes[0]
            id = int(partes[1])
            notas_cada = partes[2].split(";")
            notaTPC = float(notas_cada[0])
            notaProj = float(notas_cada[1])
            notaTeste = float(notas_cada[2])
            notas = [notaTPC, notaProj, notaTeste]
            
            aluno = (nome, id, notas)
            turma.append(aluno)
    file.close()
    return turma




op = " "
turma = []

while op != "0":
    print("---- MENU ----")
    print("1: Criar uma turma")
    print("2: Inserir um aluno na turma")
    print("3: Listar a turma")
    print("4: Consultar um aluno por id")
    print("8: Guardar a turma em ficheiro")
    print("9: Carregar uma turma dum ficheiro")
    print("0: Sair da aplicação")
    
    op = input("Insira a sua opção: ")
    if op == "1":
        turma = criar_turma()
    elif op == "2":
        turma = inserir_aluno(turma)
    elif op == "3":
        listar_turma(turma)
    elif op == "4":
        consultar_aluno(turma)
    elif op == "8":
        guardar_turma(turma)
    elif op == "9":
        turma = carregar_turma()
    else:
        print("\nOpção inválida")

if op == "0":
    print("A sair da aplicação")