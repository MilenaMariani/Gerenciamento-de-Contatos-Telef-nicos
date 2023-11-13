def criar_arquivo_lista(lista, nome_arquivo):
    with open (nome_arquivo,"w") as arquivo:
        for item_lista in lista:
            item_lista = str(item_lista)
            arquivo.write(f"{item_lista}\n") 