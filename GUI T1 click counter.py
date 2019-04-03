from tkinter import *
  
class Application:
    def __init__(self, master=None):
        self.clicks = 0
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack ()
  
    def mudarTexto(self, event):
            self.clicks += 1
            self.msg["text"] = "O botão recebeu " + str(self.clicks) + " cliques"
  
root = Tk()
Application(root)
root.mainloop()