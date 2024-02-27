import connect


def menu():
    print("Selecione a opção:")
    print(
        "[1] Cadastro de alunos | [2] Info. de alunos | [3] Modificar nota | [4] Média de notas | [0] Sair do sistema")
    menuselection = input()

    match menuselection:

        case "1":
            try:  # testa se algum valor inserido retornará um erro
                sql = "INSERT INTO alunos (nome, nota) VALUES (%s, %s)"
                val = (input("Insira o nome do aluno: "), float(input("Insira a nota do aluno: ")))
                connect.mycursor.execute(sql, val)
                connect.mydb.commit()
                print(f"Aluno incluído com sucesso!\n")
                menu()
            except ValueError:  # retorna uma mensagem de erro caso o valor inserido como nota não seja válido
                print("Valor de nota inválido!\n")
                menu()

        case "2":
            connect.mycursor.execute("SELECT COUNT(*) FROM alunos")
            results = connect.mycursor.fetchone()
            if not results:  # checa se a lista de dados não está vazia
                print("Não existem alunos cadastrados!\n")
                menu()
            else:
                connect.mycursor.execute("SELECT * FROM alunos")
                results = connect.mycursor.fetchall()
                print("Matrícula | Nome | Nota")
                for row in results:
                    print('{:} | {:} | {:}'.format(*row))
                print("\n")
                menu()

        case "3":
            if not dados:
                print("Não existem alunos cadastrados!\n")
                menu()
            else:
                try:
                    matricula = int(input("Insira a matrícula do aluno: "))

                    if matricula < len(dados):
                        novanota = float(input("Insira a nova nota: "))
                        if 0 <= novanota <= 10:  # checa se a nova nota é válida
                            dados[matricula][1] = novanota  # altera o valor do segundo dado dentro do índice
                            print(f"Nota alterada com sucesso!\n")
                            menu()
                        else:
                            print("Nota inválida, insira um valor entre 0 e 10!\n")
                            menu()
                    else:
                        print("Matrícula inválida!\n")
                        menu()
                except (ValueError, IndexError):
                    print("Valor de nota inválido!\n")
                    menu()

        case "4":
            if not dados:
                print("Não existem alunos cadastrados!\n")
                menu()
            else:
                i = soma = 0
                while i < len(dados):  # roda o loop enquanto o contador (i) for menor que o números de itens na lista
                    soma += dados[i][1]  # soma o segundo valor dos itens na lista (notas)
                    i += 1
                media = soma / i  # calcula a média usando o número de itens na lista (i)
                print(f"A média de notas é de {media:05.2f}.\n")
                menu()

        case "0":
            exit()

        case str():
            print("Opção inválida!\n")
            menu()


menu()
