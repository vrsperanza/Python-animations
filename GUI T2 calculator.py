from tkinter import *
  
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.a = Entry(self.primeiroContainer)
        self.a["width"] = 30
        self.a["font"] = self.fontePadrao
        self.a.pack(side=LEFT)

        self.b = Entry(self.segundoContainer)
        self.b["width"] = 30
        self.b["font"] = self.fontePadrao
        self.b.pack(side=LEFT)

        self.cResult = StringVar()
        self.c = Entry(self.terceiroContainer, textvariable=self.cResult)
        self.c["width"] = 30
        self.c["font"] = self.fontePadrao
        self.c.pack(side=LEFT)
  
        self.sum = Button(self.quartoContainer)
        self.sum["text"] = "+"
        self.sum["font"] = self.fontePadrao
        self.sum["command"] = self.sumMethod
        self.sum.pack()

        self.sub = Button(self.quartoContainer)
        self.sub["text"] = "-"
        self.sub["font"] = self.fontePadrao
        self.sub["command"] = self.subMethod
        self.sub.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        
    def sumMethod(self):
        self.cResult.set(str(float(self.a.get()) + float(self.b.get())))
    def subMethod(self):
        self.cResult.set(str(float(self.a.get()) - float(self.b.get())))
  
root = Tk()
Application(root)
root.mainloop()