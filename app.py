from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")

@app.route("/index")
def index():
    con = sql.connect("data.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from Vagas")
    data=cur.fetchall()
    return render_template ("index.html", datas=data)

#ADICIONAR DADOS
@app.route("/add_vaga", methods=["POST", "GET"])
def add_vaga():
    if request.method == "POST":
        cpf = request.form["CPF"]
        nome = request.form["NOME"]
        placa = request.form["PLACA"]
        modelo = request.form["MODELO"]
        horaPaga = request.form["HORA_PAGA"]

        con = sql.connect("data.db")
        cur = con.cursor()

        cur.execute("INSERT INTO Vagas(CPF, NOME, PLACA, MODELO, HORA_PAGA) values (?,?,?,?,?)", (cpf,nome,placa,modelo,horaPaga))
        con.commit()
        flash("VAGA PREENCHIDA!", "success")
        return redirect(url_for("index"))
    return render_template("add_vaga.html")

#EDITAR DADOS 
@app.route("/edit_vaga/<string:id>", methods=["POST", "GET"])
def edit_vaga(id):
    if request.method == "POST":
        cpf = request.form["CPF"]
        nome = request.form["NOME"]
        placa = request.form["PLACA"]
        modelo = request.form["MODELO"]
        horaPaga = request.form["HORA_PAGA"]

        con = sql.connect("data.db")
        cur = con.cursor()

        cur.execute("UPDATE Vagas SET CPF = ?, NOME = ?, PLACA = ?, MODELO = ?, HORA_PAGA = ? where VAGA = ?", (cpf, nome, placa, modelo, horaPaga, id))
        con.commit()
        flash("Dados atualizados", "sucess")
        return redirect(url_for("index"))
    
    con = sql.connect("data.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Vagas WHERE VAGA = ?", (id))
    data = cur.fetchone()
    return render_template("edit_vaga.html", datas=data)

#DELETAR DADOS
@app.route("/delete_vaga/<string:id>", methods = ["GET"])

def delete_vaga(id):
    con = sql.connect("data.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Vagas WHERE VAGA = ?", (id))
    con.commit()
    flash("DADOS DELETADOS", "warning")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)