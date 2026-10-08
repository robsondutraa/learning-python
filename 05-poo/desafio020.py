from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_jogos_favoritos(self, jogo):
        self.jogos_favoritos.append(jogo)
        self.jogos_favoritos = sorted(self.jogos_favoritos, key=str.lower)
    def ficha(self):
        conteudo = f"Nome Real: [black on blue] {self.nome} [/]"
        conteudo += f"\nJogos favoritos:\n"
        for jogo in self.jogos_favoritos:
            conteudo += f":video_game: [blue]{jogo}[/]\n"
        conteudo = conteudo.rstrip()
        return Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)


jogador1 = Gamer("Robson Dutra", "TazMania")
jogador1.add_jogos_favoritos("Gta V")
jogador1.add_jogos_favoritos("Cs:go 2")
jogador1.add_jogos_favoritos("Fortnite")
jogador1.add_jogos_favoritos("Elden Ring")
print(jogador1.ficha())

jogador2= Gamer("Oívia Souza", "peach_raivosa")
jogador2.add_jogos_favoritos("Call of Duty")
jogador2.add_jogos_favoritos("Mario Bros")
print(jogador2.ficha())