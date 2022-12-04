from gettext import npgettext
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas
import sqlite3 as sql

con = sql.connect("data.db")
cur = con.cursor()
selectAll = "SELECT * FROM VAGAS"
data = pandas.read_sql(selectAll, con)



# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(data.HORA_PAGA,data.MODELO)  # Plot some data on the axes.
ax.set_xlabel('HORAS PAGAS')  # Add an x-label to the axes.
ax.set_ylabel('MODELOS')  # Add a y-label to the axes.
ax.set_title("GRÁFICO DO ESTACIONAMENTO")  # Add a title to the axes.
plt.show()