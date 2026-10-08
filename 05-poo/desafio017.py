from rich.panel import Panel
from rich import print
from rich.align import Align
from rich.rule import Rule
from rich.console import Group
from rich.text import Text

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = Group(
            Align.center(self.nome),
            Rule(characters ="-", style ="none"),
            Rule(Text(f"R${self.preco:,.2f}", style="none") ,characters = ".", style = "none",)
        )

        etiqueta = Panel(conteudo, title="Produto", width=34,)
        print(etiqueta)

p1 = Produto("Iphone 17 Pro Max", 17_000.85)
p2 = Produto("Notebook Gamer",8_0_00)
p3 = Produto("TELEVISÃO LG", 2_5_00)

p1.etiqueta()
p2.etiqueta()
p3.etiqueta()