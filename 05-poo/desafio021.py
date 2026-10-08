from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def escrever(self, mensagem):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!")
        else:
            print(f"{self.cor}{mensagem}[/]", end='')

    def quebrar_linha(self, quebras = 1):
        print("\n" * quebras, end='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


caneta1 = Caneta("azul")
caneta2 = Caneta("vermelha")
caneta3 = Caneta("verde")

caneta1.destampar()
caneta2.destampar()
caneta3.destampar()

caneta1.escrever("Olá, Mundo!")
caneta2.escrever("Funciona!")
caneta2.quebrar_linha(2)
caneta3.escrever("Deu certo!")
caneta3.quebrar_linha(5)
caneta1.escrever("Será que tem faculdade?")