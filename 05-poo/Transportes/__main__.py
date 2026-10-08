from transportes import *
from rich import print
from rich.table import Table

def main():
    distancia = 11

    viagem = [Moto(distancia), Caminhao(distancia), Drone(distancia)]

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for item in viagem:
        tabela.add_row(f"{distancia}Km", f"{type(item).__name__}", f"{item.calc_frete()}")

    print(tabela)

if __name__ == "__main__":
    main()