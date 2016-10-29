from ControladorAssentos import ControladorAssento
print("---------------------------")
print("|                         |")
print("|       CINE RURAL        |")
print("|           2.0           |")
print("---------------------------")
print()
arq = open("lista.txt","r")
string = arq.read()
arq.close()
cinema = ControladorAssento()
if len(string) != 0:       #verificar se existe algo salvo no arquivo
    print("1 - Criar nova sala.")
    print("2 - Carregar sala.")
    opcao = input("Digite a opção: ")
    if opcao == "1":
        while True:
            try:
                coluna = int(input("Digite o numero de colunas: "))
                linha = int(input("Digite o numero de linhas: "))
                break
            except ValueError:
                print("Caractere invalido, tente novamente")
        lista = cinema.criaSala(coluna,linha)
        cinema.formaMatriz(coluna)

    if opcao == "2":
        cinema.carregarArquivo()
        coluna = cinema.getColuna()
        linha = cinema.getLinha()
        cinema.formaMatriz(coluna)
        
else:
    while True:
            try:
                coluna = int(input("Digite o numero de colunas: "))
                linha = int(input("Digite o numero de linhas: "))
                break
            except ValueError:
                print("Caractere invalido, tente novamente")
    lista = cinema.criaSala(coluna,linha)
    print(cinema.formaMatriz(coluna))

while True:
    print("1 - Comprar cadeira.")
    print("2 - Devolver cadeira.")
    print("3 - Resumo de vendas.")
    print("4 - Sair")
    while True:
        try:
            escolha = input("Digite sua escoha: ")
            break
        except ValueError:
            print("Caractere invalido, tente novamente.")
    if escolha == "1":
        print(cinema.formaMatriz(coluna))
        cadeiras = input("Digite as cadeiras: ")
        cadeiras = cadeiras.split(",")
        cinema.comprarCadeira(cadeiras,coluna,linha)
        

    if escolha == "2":
        cinema.formaMatriz(coluna)
        devolver = input("Digite as cadeiras: ")
        devolver = devolver.split(",")
        cinema.devolverCadeira(devolver,coluna, linha)

    if escolha == "4":
        coluna = str(coluna)
        linha = str(linha)
        cinema.salvarArquivo(coluna,linha)
        break

    if escolha == "3":
        cinema.qtdOcupados()
        print(cinema.resumoVendas())
