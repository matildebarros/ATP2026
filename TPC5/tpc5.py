'''Considere que o modelo do aluno e da turma têm a seguinte estrutura:

`aluno = (nome, id, [notaTPC, notaProj, notaTeste])`

`turma = [aluno]`

* No fim de executar a operação selecionada, a aplicação deverá colocar novamente o menu e pedir ao utilizador a opção para continuar;
* Utiliza a tua aplicação para criar uma turma com 5 alunos.'''

op = input("----MENU----\n- 1: Criar uma turma;\n- 2: Inserir um aluno na turma;\n- 3: Listar a turma;\n- 4: Consultar um aluno por id;\n- 8: Guardar a turma em ficheiro;\n- 9: Carregar uma turma dum ficheiro;\n- 0: Sair da aplicação\nInsira a sua opção: ")

if op == '1':
    turma = criar_turma()
    elif opcao == '2':
            turma = inserir_aluno(turma)
        elif opcao == '3':
            listar_turma(turma)
        elif opcao == '4':
            consultar_aluno(turma)
        elif opcao == '5':
            turma = criar_turma_exemplo_5_alunos()
        elif opcao == '8':
            guardar_turma(turma)
        elif opcao == '9':
            turma = carregar_turma()
        elif opcao == '0':
            print("\nA sair da aplicação. Até breve!")
            continuar = False
        else:
            print("\n[ERRO] Opção inválida! Por favor, tenta novamente.")
