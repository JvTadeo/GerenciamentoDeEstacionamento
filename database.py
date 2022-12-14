import sqlite3 as sql

con = sql.connect('data.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS vagas')

sql = '''CREATE TABLE IF NOT EXISTS "Vagas" 
    (
        "VAGA" INTEGER PRIMARY KEY,
        "CPF" INTEGER,
        "NOME" TEXT,
        "PLACA" TEXT,
        "MODELO" TEXT,
        "HORA_PAGA" INTEGER
    )'''

cur.execute(sql)
con.commit()
con.close()