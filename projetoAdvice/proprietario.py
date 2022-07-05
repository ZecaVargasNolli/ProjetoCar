import re

#Classe base para a manipulação de propriétario
class proprietario:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def getSelectProprietario():
        return "SELECT * FROM proprietario;"

    def getInsertProprietario():
        return "INSERT INTO proprietario (pronome, procpf) VALUES (%s, %s);"

    def validaPessoaExiste():
        return "SELECT 1 FROM proprietario WHERE pronome=%s or procpf=%s;"    
    
    def ValidaCpf(cpf):
        cpf = ''.join(re.findall(r'\d', str(cpf)))

        if not cpf or len(cpf) < 11:
            return False

        antigo = [int(d) for d in cpf]
      
        novo = antigo[:9]
        while len(novo) < 11:
            resto = sum([v * (len(novo) + 1 - i) for i, v in enumerate(novo)]) % 11

            digito_verificador = 0 if resto <= 1 else 11 - resto

            novo.append(digito_verificador)

        if novo == antigo:
            return  str(cpf)

        return False

#Classe para a apresentação dos valores de proprietário
class apresentaProprietario:
    def __init__(self, cpf, nome, quantos, apto):
        self.cpf = cpf
        self.nome = nome
        self.quantos = quantos
        self.apto = self.getApto(apto)

    def getApto(self, apto):
        if apto :
            return "SIM"
        else:
            return "NÃO"

    def formataCpf(self):
        if len(self.cpf) == 11:
            valor = self.cpf.zfill(11)
            self.cpf =  '{}.{}.{}-{}'.format(valor[:3], valor[3:6], valor[6:9], valor[9:]) 
        return self.cpf