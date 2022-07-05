from flask import Flask, render_template, redirect, url_for
from conection import Connection
from proprietario import proprietario, apresentaProprietario
from carro import carro, apresentaCarro
from flask.globals import request
from listas import Listas

app =  Flask(__name__)

# Rota central onde dará acesso as tela de proprietario e carro
@app.route("/")
def homepage():
    return render_template("principal.html")

# Rota para apresentar erros
@app.route("/erro", methods=['GET'])
def erro():
    erro = request.args.get("tipo")
    erros =  Listas()
    return render_template("erro.html", mensagem=erros.getErro(int(erro)))        

# Rota para a tela base de pessoa
@app.route("/person", methods=['GET', 'POST'])
def person():
    exe = Connection()
    result = exe.query(proprietario.getSelectProprietario())
    return render_template("pessoa.html", result=montaPessoa(result))

# Rota para a tela base de carro
@app.route("/car")
def car():
    exe = Connection()
    result = exe.query(carro.getSelectCarro())
    valores = Listas()
    resultPerson =  exe.query(proprietario.getSelectProprietario())
    return render_template("carro.html", result=montaCarro(result), resultPessoa=montaPessoaCarro(resultPerson), cor=valores.getCores(), tipo=valores.getTipos())

# Rota para cadastrar os registros de pessoa, deve validar cpf e valores preenchidos
@app.route("/cadastre", methods=['GET', 'POST'])
def insertPerson():
    nome = request.form.get("name")
    cpf = request.form.get("cpf")
    if(cpf == None or nome == None):
        return redirect("http://localhost:5000/erro?tipo=2")
    nome = nome.upper()    
    pessoa = proprietario(cpf, nome)
    pessoa.cpf =  proprietario.ValidaCpf(pessoa.cpf)    
    if pessoa.cpf:
        exe = Connection()
        valido = exe.query(proprietario.validaPessoaExiste(), (nome, cpf))
        if(len(valido) == 0):
            exe.execute(proprietario.getInsertProprietario(), (nome, cpf))
            exe.commit()
            return redirect("http://localhost:5000/person")
        else:
            return redirect("http://localhost:5000/erro?tipo=3")        
    else:
        return redirect("http://localhost:5000/erro?tipo=1")

# Rota para cadastrar os registros de carro, deve validar valores preenchidos
@app.route("/cadastraCarro", methods=['GET', 'POST'])
def insertCar():
    cpf = request.form.get("cpf")
    cor = request.form.get("cor")
    tipo = request.form.get("tipo")
    if(cpf == None or cor == None or tipo == None):
        return redirect("http://localhost:5000/erro?tipo=2")
    
    exe = Connection()
    cpf = proprietario.ValidaCpf(cpf)
    resultPerson =  exe.query(proprietario.getSelectProprietario())
    exe.execute(carro.getInsertCarro(), ((len(resultPerson) + 1), tipo, cor, cpf))
    exe.commit()

    return redirect("http://localhost:5000//car")   

# Rota para deletar os registros de carro deve validar se existe o valor de id
@app.route("/deletarCarro", methods=['GET', 'POST'])
def deletaCar():
    id = request.args.get("id")
    if(id == None):
        return redirect("http://localhost:5000/erro?tipo=2")  
    exe = Connection()
    exe.execute(carro.getDeleteCarro(), (id))
    exe.commit()
   
    return redirect("http://localhost:5000/car")   

#Método para filtrar para utilizar somente pessoa que não possuem 3 carros na rotina de inclusão de carro
def montaPessoaCarro(result):
    resultado = montaPessoa(result)
    apresentar = []
    for res in resultado:
        if int(res.quantos[0]) != 3:
            apresentar.append(res)

    return apresentar

#Método para montar o formato de apresentação de pessoa
def montaPessoa(result):
    pessoaApresenta = []
    for res in result:
        exe = Connection()
        result = exe.query("SELECT count(carid) FROM carro WHERE procpf = '" + res[1] + "'", res)
        aprePerson = apresentaProprietario(res[1], res[0], result[0], (result[0][0] == 0))
        aprePerson.formataCpf()
        pessoaApresenta.append(aprePerson)
    return pessoaApresenta

#Método para montar o formato de apresentação de carro
def montaCarro(result):
    carroApresenta = []
    for res in result:
        car =  carro(*res)
        exe = Connection()
        valores = Listas()
        retorno = exe.query("SELECT pronome FROM proprietario WHERE procpf = '" + res[3] + "'", res)
        apreCar = apresentaCarro(car.id, retorno[0][0], valores.getCor(car.cor), valores.getTipo(car.tipo))
        carroApresenta.append(apreCar)
    return carroApresenta

if __name__ == "__main__":
    app.run()