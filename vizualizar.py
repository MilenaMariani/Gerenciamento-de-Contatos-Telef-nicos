def visualizarLista():
    with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/AgendaDeContato/contatos.txt', 'r') as ler_arquivo:
        for linha in ler_arquivo:
            print(linha)