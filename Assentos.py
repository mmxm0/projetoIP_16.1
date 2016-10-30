class Assento:
    def __init__(self,numero,preco,disponivel):
        self.__numero = numero
        self.__preco = preco
        self.__disponivel = disponivel

    def getNumero(self):
        return self.__numero

    def setNumero(self,novoNumero):
        self.__numero = novoNumero

    def getPreco(self):
        return self.__preco

    def setPreco(self,novoPreco):
        self.__preco = novoPreco

    def getDisponivel(self):
        return self.__disponivel

    def setDisponivel(self,seDisponivel):
        self.__disponivel = seDisponivel
