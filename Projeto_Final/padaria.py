import os #biblioteca importada para usar o comando "system"

produtos = [] #lista para armazenar os produtos
vendas = [] #lista para armazenar os registros de vendas

os.system("cls") or None #comando usado para limpar a tela antes de rodar o programa

def menu(): #função pra exibir o menu principal
    print("\n=<>=<>= PADARIA CÉU =<>=<>=\n\n1 - Cadastrar Produto\n2 - Alterar Produto\n3 - Realizar Venda\n4 - Relatórios\n5 - Sair")

def casdastrar_produto(): #função para cadastrar um produto
    os.system("cls") or None
    print("\n-=-= CADASTRAR PRODUTO =-=-")

    nome = input("Nome do produto: ")
    while not nome.replace(" ", "").isalpha(): #verifica se a resposta contém apenas letras
        print("\n\033[91m{}\033[00m".format("Nome inválido! Digite apenas letras")) #imprime uma mensagem na cor vermelha
        nome = input("\nNome do Produto: ")

    tipo = input("Tipo do produto: ")
    while not tipo.replace(" ", "").isalpha():
        print("\n\033[91m{}\033[00m".format("Tipo inválido! Digite apenas letras")) #imprime uma mensagem na cor vermelha
        tipo = input("\nTipo do Produto: ")

    preco = input("Preço do produto: ")
    while not preco.replace(".", "").isnumeric(): #verifica se a resposta contém apenas números
        print("\n\033[91m{}\033[00m".format("Preço inválido! Digite um número")) #imprime uma mensagem na cor vermelha
        preco = input("\nPreço do Produto: ")

    estoque = input("Estoque do produto: ")
    while not estoque.isnumeric():
        print("\n\033[91m{}\033[00m".format("Estoque inválido! Digite um número inteiro")) #imprime uma mensagem na cor vermelha
        estoque = input("\nEstoque do Produto: ")

    preco = float(preco) #transforma a variável em um número flutuante
    estoque = int(estoque) #transforma a variável em um número inteiro

    if nome and tipo and preco and estoque: #verifica se os quatro campos foram preenchidos
        produto = {"id": len(produtos) + 1, "nome": nome, "tipo": tipo, "preco": preco, "estoque": estoque} #cria um dicionário com as informações e gera um identificador para o produto
        produtos.append(produto) #adiciona o dicionário dentro da lista de produtos
        print("\n\033[92m{}\033[00m".format("Produto cadastrado!")) #imprime uma mensagem na cor verde

def alterar_produto(): #função para alterar um produto
    os.system("cls") or None
    print("\n-=-= ALTERAR PRODUTO =-=-")
    opcao = input("Deseja buscar o produto pelo nome (N) ou pelo identificador (I)? ")

    if opcao.upper() == "N":
        nome_do_produto = input("Digite o nome do produto: ")
        produto_encontrado = None
        for produto in produtos:
            if produto["nome"].lower() == nome_do_produto.lower():
                produto_encontrado = produto
                break
    elif opcao.upper() == "I":
        id_do_produto = input("Digite o identificador do produto: ")
        while not id_do_produto.isnumeric():
            print("\n\033[91m{}\033[00m".format("Resposta inválida! Você deve digitar um número inteiro.")) #imprime uma mensagem na cor vermelha
            id_do_produto = input("\nDigite o identificador do produto: ")
        
        id_do_produto = int(id_do_produto)

        produto_encontrado = None
        for produto in produtos:
            if produto["id"] == id_do_produto:
                produto_encontrado = produto
                break
    else:
        print("\n\033[91m{}\033[00m".format("Opção inválida!")) #imprime uma mensagem na cor vermelha
        return
        
    if produto_encontrado:
        print(f"\nProduto econtrado:\nID: {produto_encontrado['id']}\nNome: {produto_encontrado['nome']}\nTipo: {produto_encontrado['tipo']}\nPreço: {produto_encontrado['preco']}\nEstoque: {produto_encontrado['estoque']}")

        opcao_alterar = input("\nDeseja alterar os dados do produto (S/N)? ")
        if opcao_alterar.upper() == "S":
            print("\nSelecione a informação do produto que deseja alterar:\n1 - Nome\n2 - Tipo\n3 - Preço\n4 - Estoque")

            opcao_informacao = input("Opção: ")

            if opcao_informacao == "1":
                novo_nome = input("\nDigite o novo nome: ")
                while not novo_nome.replace(" ", "").isalpha():
                    print("\n\033[91m{}\033[00m".format("Nome inválido!")) #imprime uma mensagem na cor vermelha
                    nome = input("\nDigite o novo nome: ")
                produto_encontrado["nome"] = novo_nome

            elif opcao_informacao == "2":
                novo_tipo = input("\nDigite o novo tipo: ")
                while not novo_tipo.replace(" ", "").isalpha():
                    print("\n\033[91m{}\033[00m".format("Tipo inválido!")) #imprime uma mensagem na cor vermelha
                    nome = input("\nDigite o novo tipo: ")
                produto_encontrado["tipo"] = novo_tipo

            elif opcao_informacao == "3":
                novo_preco = input("\nDigite o novo preço: ")
                while not novo_preco.replace(".", "").isnumeric():
                    print("\n\033[91m{}\033[00m".format("Preço inválido!")) #imprime uma mensagem na cor vermelha
                    preco = input("\nDigite o novo preço: ")
                produto_encontrado["preco"] = novo_preco
                novo_preco = float(novo_preco)

            elif opcao_informacao == "4":
                novo_estoque = input("\nDigite o novo estoque: ")
                while not novo_estoque.replace(".", "").isnumeric():
                    print("\n\033[91m{}\033[00m".format("Estoque inválido!")) #imprime uma mensagem na cor vermelha
                    preco = input("\nDigite o novo estoque: ")
                produto_encontrado["estoque"] = novo_estoque
                novo_estoque = int(novo_estoque)

            else:
                print("\n\033[91m{}\033[00m".format("Opção inválida!")) #imprime uma mensagem na cor vermelha

            print("\n\033[92m{}\033[00m".format("Produto alterado!")) #imprime uma mensagem na cor verde
        else:
            print("\n\033[91m{}\033[00m".format("Alteração cancelada")) #imprime uma mensagem na cor vermelha
    else:
        print("\n\033[91m{}\033[00m".format("Produto não econtrado!")) #imprime uma mensagem na cor vermelha

def realizar_venda(): #função para realizar uma venda
    os.system("cls") or None #limpa a tela
    print("\n-=-= REALIZAR VENDA =-=-\n")
    for produto in produtos:
        print(f"{produto['id']} - {produto['nome']} - (Estoque: {produto['estoque']})") #imprime as informações de cada produto separadas por traços
    
    id_do_produto = input("\nDigite o ID do produto a ser vendido: ")
    while not id_do_produto.isnumeric():
        print("\n\033[91m{}\033[00m".format("Resposta inválida! Você deve digitar um número inteiro.")) #imprime uma mensagem na cor vermelha
        id_do_produto = input("\nDigite o ID do produto a ser vendido: ")

    id_do_produto = int(id_do_produto)

    quantidade = input("Digite a quantidade desejada: ")
    while not quantidade.isnumeric():
        print("\n\033[91m{}\033[00m".format("Resposta inválida! Você deve digitar um número inteiro.")) #imprime uma mensagem na cor vermelha
        quantidade = input("\nDigite a quantidade desejada: ")

    quantidade = int(quantidade)

    produto_escolhido = None
    for produto in produtos:
        if produto["id"] == id_do_produto:
            produto_escolhido = produto
            break
    
    if produto_escolhido:
        if quantidade <= produto_escolhido["estoque"]:
            produto_escolhido["estoque"] = produto_escolhido["estoque"] - quantidade

            venda = {"produto": produto_escolhido, "quantidade": quantidade, "total": produto_escolhido["preco"] * quantidade}
            vendas.append(venda)

            print("\n\033[92m{}\033[00m".format("Venda realizada com sucesso!")) #imprime uma mensagem na cor verde
        else:
            print("\n\033[91m{}\033[00m".format("Atenção: a quantidade solicitada é maior que o estoque disponível!")) #imprime uma mensagem na cor vermelha
    else:
        print("\n\033[91m{}\033[00m".format("Produto não econtrado!")) #imprime uma mensagem na cor vermelha
        
def gerar_relatorios(): #função para gerar relatórios
    os.system("cls") or None
    print("\n-=-= RELATÓRIOS =-=-\n\n1 - Relatório de todos os produtos\n2 - Relatório de vendas realizadas")

    opcao = input("Oção: ")

    if opcao == "1":
        print("\nRelatório de produtos:")
        print("{:<5} {:<15} {:<15} {:<10} {:<10}".format("ID", "Nome", "Tipo", "Preço", "Estoque")) #define o espaço entre cada título
        for produto in produtos:
            print("{:<5} {:<15} {:<15} {:<10} {:<10}".format(produto["id"], produto["nome"], produto["tipo"], produto["preco"], produto["estoque"])) #define o espaço entre cada informação

    elif opcao == "2":
        print("\nRelatório de vendas:")
        print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Produto", "Quantidade", "Total")) #define o espaço entre cada título
        for l, venda in enumerate(vendas, start = 1):
            produto = venda["produto"]
            quantidade = venda["quantidade"]
            total = venda["total"]
            print("{:<5} {:<20} {:<10} {:<10}".format(l, produto["nome"], quantidade, total)) #define o espaço entre cada informação
    else:
        print("\n\033[91m{}\033[00m".format("Opção inválida!")) #imprime uma mensagem na cor vermelha

while True: #loop para iniciar o programa e para voltar ao menu principal sempre que encerrar uma ação
    menu() #chama a função menu
    opcao = input("Opção: ")

    if opcao == "1":
        casdastrar_produto() #chama a função cadastrar_produto
    elif opcao == "2":
        alterar_produto() #chama a função alterar_produto
    elif opcao == "3":
        realizar_venda() #chama a função realizar_venda
    elif opcao == "4":
        gerar_relatorios() #chama a função gerar_relatorios
    elif opcao == "5":
        print("\nAté a próxima...") #imprime a mensagem de encerramento do programa
        break
    else:
        print("\n\033[91m{}\033[00m".format("Opção inválida!")) #imprime uma mensagem na cor vermelha
