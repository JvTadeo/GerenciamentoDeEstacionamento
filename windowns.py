from tkinter import * 
import database

root = Tk()
root.title("SISTEMA DE ESTACIONAMENTO")
root.geometry("640x520")
root.resizable(False, False)

class MainWindows(Tk):
    def __init__(self, root):
        #DECLANDO BOTÕES
        self.nameSystem = Label(root, text="GERENCIAMENTO DO ESTACIONAMENTO", font=('Roboto', 15), fg = 'white', bg='#CF0A0A', width=100, height=2, anchor=W, padx = 10)

        self.vaga1 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1, command= lambda : NewWindow.WindowDefautl())
        self.vaga2 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1, command= lambda : NewWindow.WindowDefautl())
        self.vaga3 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1, command= lambda : NewWindow.WindowDefautl())
        self.vaga4 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1, command= lambda : NewWindow.WindowDefautl())
        self.vaga5 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1, command= lambda : NewWindow.WindowDefautl())
        self.vaga6 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1, command= lambda : NewWindow.WindowDefautl())

        self.nameSystem.grid(column=1, row=0, columnspan = 30)

        #COLOCANDO OS BOTÕES
        self.vaga1.place(x=130, y=120)
        self.vaga2.place(x=280, y=120)
        self.vaga3.place(x=430, y=120)

        self.vaga4.place(x=130, y=290)
        self.vaga5.place(x=280, y=290)
        self.vaga6.place(x=430, y=290) 
    



class NewWindow():
    def WindowDefautl():
        newRoot = Toplevel()
        newRoot.geometry("440x210")
        newRoot.resizable(False, False)
        newRoot.configure(bg='#D9D9D9')
        newRoot.title("CADASTRO DE CARROS")

        nome = Label(newRoot, text="Nome", font=('Roboto', 15), fg = 'black', bg='#D9D9D9')
        Modelo = Label(newRoot, text="Modelo", font=('Roboto', 15), fg = 'black',padx=2, bg='#D9D9D9', anchor=N)
        Placa = Label(newRoot, text="Placa", font=('Roboto', 15), fg = 'black',padx=2, bg='#D9D9D9', anchor=N)
        HoraEntrada = Label(newRoot, text="Hora Da Entrada", font=('Roboto', 15), fg = 'black',padx=5, bg='#D9D9D9', anchor=N)

        nomeEntry = Entry(newRoot, font=('Roboto', 15), bd=-1)
        modeloEntry = Entry(newRoot, font=('Roboto', 15), bd=-1, width=8)
        placaEntry = Entry(newRoot, font=('Roboto', 15), bd=-1, width=8)
        horaEntradaEntry = Entry(newRoot, font=('Roboto', 15), bd=-1, width=8)

        concluir = Button(newRoot, bg="#00C130", width=25, height=2, relief = GROOVE, bd = -1, text="CONCLUIR", font=('Roboto', 10), fg='#FFFFFF', command= lambda: database.insert(nomeEntry.get(), modeloEntry.get(), placaEntry.get(), horaEntradaEntry.get()))
        
        nome.grid(column=1, row=1)
        Modelo.grid(column=1, row=2)
        Placa.grid(column=1, row=3)
        HoraEntrada.grid(column=1, row=4)

        nomeEntry.grid(column=2, row=1)
        modeloEntry.grid(column=2, row=2, sticky=W)
        placaEntry.grid(column=2, row=3, sticky=W)
        horaEntradaEntry.grid(column=2, row=4, sticky=W)

        concluir.place(x = 120, y = 150)

        
    
        


exec = MainWindows(root)
root.mainloop()

