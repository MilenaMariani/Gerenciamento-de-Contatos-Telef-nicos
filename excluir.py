import ast

def excluirUsuario(contato_escolhido):
    
    with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/AgendaDeContato/contatos.txt', 'r') as lista_alunos:
        for linha in lista_alunos:
            if contato_escolhido in linha:

                contato = ast.literal_eval(linha)

                del contato

                return contato