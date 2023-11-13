def adicionarUsuario():
    with open ('manipulaçãoDeArquivos/listaExerciciosManipulacao/AgendaDeContato/contatos.txt', 'w') as listaDeContatos:
            
            nome_contato = input("Digite o nome do contato: ")
            ddd_contato = int(input("Digite o DDD: "))
            numero_contato = int(input("Digite o número do telefone: "))
            endereco_contato = input("Digite o endereço do contato: ")

            contato = {
                "nome": nome_contato,
                "ddd": ddd_contato,
                "numero": numero_contato,
                "endereco": endereco_contato
            }
            
    return contato

def adicionarVarios():
    quantidade_de_contatos = int(input("Digite a quantidade de contatos à adicionar: "))
    alunos = []
    for x in range (0,quantidade_de_contatos):
        aluno = adicionarUsuario()
        alunos.append (aluno)
    
    return alunos