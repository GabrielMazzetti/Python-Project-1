import tkinter as tk

class Application:
    def __init__(self, master=None):
            self.fontePadrao = ("Arial", "10")
            self.primeiroContainer = tk.Frame(master)
            self.primeiroContainer["pady"] = 10
            self.primeiroContainer.pack()

            self.segundoContainer = tk.Frame(master)
            self.segundoContainer["padx"] = 20
            self.segundoContainer.pack()

            self.terceiroContainer = tk.Frame(master)
            self.terceiroContainer["padx"] = 20
            self.terceiroContainer.pack()

            self.quartoContainer = tk.Frame(master)
            self.quartoContainer["pady"] = 20
            self.quartoContainer.pack()

            self.titulo = tk.Label(self.primeiroContainer, text="Dados do usuario")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()

            self.nomeLabel = tk.Label(self.segundoContainer,text="Nome", font= self.fontePadrao[0])
            self.nomeLabel.pack(side= tk.LEFT)

            self.nome = tk.Entry(self.segundoContainer)
            self.nome["width"] = 30
            self.nome["font"] = self.fontePadrao
            self.nome.pack(side= tk.LEFT)

            self.senhaLabel = tk.Label(self.terceiroContainer, text="Senha", font=self.fontePadrao[0])
            self.senhaLabel.pack(side= tk.LEFT)

            self.senha = tk.Entry(self.terceiroContainer)
            self.senha["width"] = 30
            self.senha["font"] = self.fontePadrao
            self.senha["show"] = "*"
            self.senha.pack(side= tk.LEFT)

            self.autenticar = tk.Button(self.quartoContainer)
            self.autenticar["text"] = "Autenticar"
            self.autenticar["font"] = ("Calibri", "8")
            self.autenticar["width"] = 12
            self.autenticar["command"] = self.verificaSenha
            self.autenticar.pack()

            self.mensagem = tk.Label(self.quartoContainer, text="", font=self.fontePadrao[0])
            self.mensagem.pack()

    #M�todo verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "Gabriel" and senha == "ngnl":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro no login ou senha"
root = tk.Tk()
Application(root)
root.mainloop()
 



