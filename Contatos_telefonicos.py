from excluir import excluirUsuario
from atualizar import atualizarLista
from adicionar import adicionarUsuario, adicionarVarios
from visualizar import visualizarLista
from criar_arquivo import criar_arquivo_lista

print("----Sistema de Agenda----")
print("---O que deseja fazer:---")

escolha_usuario = int(input("Digite 1 para Adicionar \nDigite 2 para Visualizar \nDigite 3 para Atualizar \nDigite 4 para Excluir \nDigite 0 para encerrar\n"))

resp = 1

while resp != 0:
    
    if escolha_usuario == 1:
        quant_usuarios = int(input("Digite 1 para adicionar apenas 1 contatos \nDigite 2 para adicionar 2 ou mais usuarios: "))

        if quant_usuarios == 1:
            dados = adicionarUsuario()
        elif quant_usuarios == 2:
            dados = adicionarVarios()

        criar_arquivo_lista(lista=dados, nome_arquivo="manipulaçãoDeArquivos/listaExerciciosManipulacao/AgendaDeContato/contatos.txt") 

        resp = int(input("Digite 0 para encerrar \nDigite 1 para continuar \n"))

    elif escolha_usuario == 2:
        visualizarLista()
        break

    elif escolha_usuario == 3:
        visualizarLista()
        escolher_contato = input("Qual usuario deseja atualizar: ")
        atualizarLista(contato_escolhido=escolher_contato)
        break

    elif escolha_usuario == 4:
        escolher_contato = input("Qual usuario deseja excluir: ")
        excluirUsuario(contato_escolhido=escolher_contato)
        break

    elif escolha_usuario == 0:
        break
    else:
        print("Escolha Inválida!")