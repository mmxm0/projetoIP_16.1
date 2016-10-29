from Assentos import Assento
class ControladorAssento:
        def __init__(self,listaAssentos = [],renda = 0,devolvidos = 0):
                self.__listaAssentos = listaAssentos
                self.__renda = renda
                self.__devolvidos = devolvidos
                self.__ocupacao = 0

        def getListaAssentos(self):
            return self.__listaAssentos

        def getColuna(self):
            arquivo = open("lista.txt", "r")
            c = arquivo.readline()
            coluna = arquivo.readline()
            coluna = int(coluna)
            return coluna

        def getLinha(self):
            arquivo = open("lista.txt","r")
            linha = arquivo.readline()
            return linha

        def qntOcupados(self):
            cont = 0
            for i in self.__listaAssentos:
                if i.getDisponivel() == "0":
                        cont += 1
            return("Quantidade de cadeiras ocupadas %d" %cont)

        def criaSala(self, coluna, linha):#Recebe uma listaVazia, e adiciona obejos assentos em uma lista vazia
                valor = 20
                contador = 0
                if coluna > 20:
                        print("ERRO:\nSua sala não pode ter mais que 20 linhas.")
                else: 
                        for i in range(coluna*linha): 
                            string = str(i).rjust(len(str(coluna*linha)),"0")
                            if contador == coluna:
                                valor -= 1
                                assento = Assento(string,valor,"1")
                                self.__listaAssentos.append(assento)
                                contador = 0
                            else:
                                assento = Assento(string,valor,"1")
                                self.__listaAssentos.append(assento)        
                            contador += 1
                
        def formaMatriz(self, coluna):#Cria uma matriz com os lugares do cinema para ser impressa
                matriz = ""
                contador = 0
                for i in self.__listaAssentos:
                        if contador == coluna:
                                matriz += "\n"
                                contador = 0
                        matriz += i.getNumero() + " "
                        contador +=1
                return matriz

        def comprarCadeira(self,cadeiras,coluna,linha):
                podeComprar = True
                for i in cadeiras:
                        valor = int(i)
                        if valor > len(self.__listaAssentos):
                                print("Você não pode comprar o assento %s" %i)
                                podeComprar = False
                        elif self.__listaAssentos[valor].getDisponivel() != "1":
                                print("Você não pode comprar o assento %s" %i)
                                podeComprar = False
                if podeComprar:
                        for i in cadeiras:
                                valor = int(i)
                                print("Você comprou a cadeira %s " %i)
                                self.__listaAssentos[valor].setDisponivel("0")
                                self.__listaAssentos[valor].setNumero("x"*len(str(coluna*linha)))
                                self.__renda += self.__listaAssentos[valor].getPreco()

        def devolverCadeira(self,cadeiras, coluna, linha):
                podeDevolver = True
                for i in cadeiras:
                        valor = int(i)
                        if self.__listaAssentos[valor].getDisponivel() != "0":
                                print("Esta cadeira não foi comprada.")
                                podeDevolver = False
                                
                if podeDevolver:
                        for i in cadeiras:
                                valor = int(i)
                                print("Você devolveu a cadeira %s" %i)
                                self.__listaAssentos[valor].setDisponivel("1")
                                self.__listaAssentos[valor].setNumero((str(valor)).rjust(len(str(coluna*linha)),"0"))
                                self.__renda -= (0.9*self.__listaAssentos[valor].getPreco())
                                self.__devolvidos += 1

        def qtdOcupados(self):
            cont = 0
            for cadeira in self.__listaAssentos:
                if cadeira.getDisponivel() == "0":
                    cont += 1
            self.__ocupacao = cont

        def resumoVendas(self):
            resumo = "Ocupação da sala no momento: %i\nQuantidade de ingressos devolvidos: %i \nValor total apurado: %.2f" % (self.__ocupacao, self.__devolvidos, self.__renda)
            return resumo

        def salvarArquivo(self,coluna,line):
                arquivo = open("lista.txt", "w")
                arquivo.write(line+"\n")
                arquivo.write(coluna+"\n")
                for assento in self.__listaAssentos:
                        linha = ""
                        linha += str(assento.getNumero())
                        linha += ":"
                        linha += str(assento.getPreco())
                        linha += ":"
                        linha += str(assento.getDisponivel())
                        arquivo.write(linha)
                        arquivo.write("\n")
                linha = ""
                linha += str(self.__devolvidos)
                linha += "*"
                linha += str(self.__renda)                
                arquivo.write(linha)
                arquivo.close()
                        
        def carregarArquivo(self):
            arquivo = open("lista.txt", "r")
            pulaLinha = arquivo.readline() #serve apenas para pular uma linha
            pulacoluna = arquivo.readline()
            lista = arquivo.read()
            lista = lista.split("\n")
            l = lista.pop(-1)
            l = l.split("*")
            self.__devolvidos = int(l[0])
            self.__renda= float(l[1])
            listaObject = []
            for assento in lista:
                info = assento
                info = info.split(":")
                info[1] = float(info[1])
                cadeira = Assento(info[0], info[1], info[2])
                listaObject.append(cadeira)
            self.__listaAssentos = listaObject
            arquivo.close()
            
                
        




                        
        
        





  
                    







