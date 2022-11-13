from tkinter import * 


root = Tk()
root.title("SISTEMA DE ESTACIONAMENTO")
root.geometry("640x520")

photo1 = PhotoImage(file='Imagens\Car.png')


class MainWindows(Tk):
    def __init__(self, root):

        self.nameSystem = Label(root, text="GERENCIAMENTO DO ESTACIONAMENTO", font=('Roboto', 15), fg = 'white', bg='#CF0A0A', width=100, height=2, anchor=W, padx = 10)

        self.vaga1 = Button(bg="#00C130")
        self.vaga2 = Button(bg="#00C130")
        self.vaga3 = Button(bg="#00C130")
        self.vaga4 = Button(bg="#00C130")
        self.vaga5 = Button(bg="#00C130")
        self.vaga6 = Button(bg="#00C130")


        self.nameSystem.grid(column=1, row=0, columnspan = 10)
        self.vaga1.grid(column=1, row=1, sticky=W, padx=20, pady=50)
        self.vaga2.grid(column=2, row=1, sticky='')
        self.vaga3.grid(column=3, row=1, sticky=E)
        self.vaga4.grid(column=1, row=2, sticky=W, padx=20, pady=50)
        self.vaga5.grid(column=2, row=2, sticky='')
        self.vaga6.grid(column=3, row=2, sticky=E)
        
            

        
        

exec = MainWindows(root)
root.mainloop()

