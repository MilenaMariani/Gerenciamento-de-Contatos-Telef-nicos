import ast

def atualizarLista(contato_escolhido):
    escolha_atualizar = int(input("Digite 1 para atualizar o nome \nDigite 2 para atualizar o ddd \nDigite 3 para atualizar o numero \nDigite 4 para atualizar o endereço \n"))

    with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/AgendaDeContato/contatos.txt', 'r') as lista_alunos:
        for linha in lista_alunos:
            if contato_escolhido in linha:

                contato = ast.literal_eval(linha)

                if (escolha_atualizar == 1):
                    contato["nome"] = input("Digite o novo nome: ")
                elif (escolha_atualizar == 2):
                    contato["ddd"] = int(input("Digite o novo ddd: "))
                elif (escolha_atualizar == 3):
                    contato["numero"] = int(input("Digite o novo numero: "))
                elif (escolha_atualizar == 4):
                    contato["endereco"] = input("Digite novo endereço: ")

                print(contato)

                return contato
            