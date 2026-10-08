from abc import ABC,abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):

    salario_min = 1612
    inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):

        self.salario = self.calc_sal()
        qtd_salarios_min = self.salario / Funcionario.salario_min

        conteudo = f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) "
        conteudo += f"é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{qtd_salarios_min:.1f} salários mínimos.[/]"
        painel = Panel(conteudo, title=" Análise de Salário ", width= 50)

        print(painel)


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, horas_trab = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab

    def calc_sal(self):
        return self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)



class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto =  sal_bruto

    def calc_sal(self):
        inss = self.sal_bruto * self.inss / 100
        return self.sal_bruto - inss