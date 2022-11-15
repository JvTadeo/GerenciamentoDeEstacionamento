import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute("CREATE TABLE if not exists carro(placa TEXT PRIMARY KEY, modelo TEXT,  HrEntrada REAL, nome TEXT)")
#textar se a tabela foi criada
#res = cur.execute("SELECT carro FROM sqlite_master")
#res.fetchone()

cur.execute('''
    INSERT or ignore  INTO carro VALUES
        ('GOL1234','GOL',19.58,'LUCA'),
        ('FOX1234','FOX',19.59,'TADEO')
''')
#confirmar o q foi feito
con.commit()
#vericar dado inserido
res = cur.execute("SELECT * FROM carro")
res.fetchall()

data = [
    ('GOLF123','GOLF',20.04,'FERRETI'),
    ('X412345','X4',20.05,'FELIPE'),
]
#cur.executemany("INSERT INTO carro VALUES(?, ?, ?, ?)", data)
con.commit()  # Lembre-se de confirmar a transação após executar INSERT.
#print tudo
for row in cur.execute("SELECT * FROM carro ORDER BY placa"):
    print(row)

con.close()
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT placa, HrEntrada FROM carro ORDER BY HrEntrada asc b ")
Cplaca, hora = res.fetchone()
print(f'O carro {Cplaca!r} entrou {hora}')

