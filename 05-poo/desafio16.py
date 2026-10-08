from rich import print

class Funcionario:
    
    # Atributos de Classes
    empresa = "Curso em Vídeo"

    """
    Classe onde podemos cadastrar funcionários por nome, cargo e setor.
    """
    def __init__(self, nome, setor, cargo): #Método contrutor
        # Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"\n:handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}."


#Objeto
cargo1 = Funcionario("Gabriel", "TI", "Programador")
print(cargo1.apresentacao())

cargo2 = Funcionario("Gabriela", "Empresas", "Contadora")
print(cargo2.apresentacao())
