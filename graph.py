import matplotlib.pyplot as plt
import pandas
import sqlite3 as sql

con = sql.connect("data.db")
cur = con.cursor()
selectAll = "SELECT * FROM VAGAS"
data = pandas.read_sql(selectAll, con)



fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(data.MODELO,data.HORA_PAGA)
ax.set_xlabel('HORAS PAGAS') 
ax.set_ylabel('MODELOS')  # Add a y-label to the axes.
ax.set_title("GRÁFICO DO ESTACIONAMENTO")  # Add a title to the axes.
plt.show()