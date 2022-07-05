#Classe para a manipulação de proprietário
class carro:
    def __init__(self, id, tipo, cor, Dono):
        self.id = id
        self.tipo = tipo
        self.cor = cor
        self.Dono = Dono

    def getSelectCarro():
        return "SELECT * FROM carro;"    

    def getInsertCarro():
        return "INSERT INTO carro(carid, cartipo, carcor, procpf) VALUES (%s, %s, %s, %s)"

    def getDeleteCarro():
        return "DELETE FROM carro WHERE carid=%s"

#Classe para a apresentação dos valores de proprietário
class apresentaCarro:
    def __init__(self, id, nomeProprietario, cor, tipo):
        self.id = id
        self.nomeProprietario = nomeProprietario
        self.cor = cor
        self.tipo = tipo
    