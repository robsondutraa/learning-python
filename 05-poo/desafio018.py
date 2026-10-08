from rich import print
from rich.panel import Panel

class Churrasco:
    #Atributos de Classe
    consumo_padrao:float = 0.400 # Cada pessoa come 400 gramas de carne.
    preco_kg:float = 82.40 # Cada kg de carne custa 82.40

    def __init__(self, titulo, quantidade) :
        #Metódo de Instanciâmento
        self.titulo = titulo
        self.participantes = quantidade

    def __str__(self):
        return f"Esse é {self.titulo} com {self.participantes} participantes "

    def calcular_quant_carne(self) -> float:
        return self.participantes * self.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_quant_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = (f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]"
                    f"\nCada participante comerá 0.4Kg e cada Kg custa R$82.40"
                    f"\nRecomendo [blue]comprar {self.calcular_quant_carne():,.3f}Kg[/] de carne"
                    f"\nO custo total será de [green]{self.calcular_custo_total():,.2f}[/]"
                    f"\nCada pessoa pagará [yellow]{self.calcular_custo_individual()}R$[/]."
                    )
        painel = Panel(conteudo, title=self.titulo)
        print(painel)



churrasco1 = Churrasco("Churra dos amigos", 15)
churrasco1.analisar()


churrasco2 = Churrasco("Festa do Fim de Ano", 80)
churrasco2.analisar()