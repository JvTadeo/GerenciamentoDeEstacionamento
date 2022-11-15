from tkinter import * 
import cadastroDeCarros

root = Tk()
root.title("SISTEMA DE ESTACIONAMENTO")
root.geometry("640x520")
root.resizable(False, False)

class MainWindows(Tk):
    def __init__(self, root):
        #DECLANDO BOTÕES
        self.nameSystem = Label(root, text="GERENCIAMENTO DO ESTACIONAMENTO", font=('Roboto', 15), fg = 'white', bg='#CF0A0A', width=100, height=2, anchor=W, padx = 10)

        self.vaga1 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1, command= lambda : NewWindow.WindowDefautl())
        self.vaga2 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1)
        self.vaga3 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1)
        self.vaga4 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1)
        self.vaga5 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1)
        self.vaga6 = Button(bg="#00C130", width=9, height=8, relief = GROOVE, bd = -1)

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
        newRoot.geometry("340x230")
        newRoot.resizable(False, False)
        newRoot.configure(bg='#D9D9D9')
        newRoot.title("CADASTRO DE CARROS")

        nome = Entry(newRoot, )

        nome.grid(column=1, row=0)
        
        
    
        


exec = MainWindows(root)
root.mainloop()

