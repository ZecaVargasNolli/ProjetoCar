#Listas para tratametno de valores no sistema
class Listas():
    def __init__(self):
        self.cor = [[1, "Yellow"], [2, "Gray"], [3, "Blue"]]
        self.tipo = [[1, "Hatch"], [2, "Sedan"], [3, "Convertible"]]
        self.erro = [[1, "CPF Inválido"], [2, "Todos os valores Obrigatórios não foram informados"], [3, "Já existe uma pessoa com este nome"]]

    def getCores(self):
        return self.cor

    def getCor(self, indice):
        return self.getCores()[indice-1][1]

    def getTipos(self):
        return self.tipo

    def getTipo(self, indice):
        return self.getTipos()[indice-1][1]
    
    def getErros(self):
            return self.erro

    def getErro(self, indice):
        return self.getErros()[indice-1][1]