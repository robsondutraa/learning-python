from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que "
              f"tem [green]{self.total_paginas} páginas[/] no total. Você agora está na "
              f"[yellow]página {self.pagina_atual}[/]"
              )

    def avancar_paginas(self, quantidade = 1):
        contador = 0
        for pag in range(0, quantidade, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end='')
                sleep(0.2)
                contador += 1
        print(f"[blue]Você avançou {contador} páginas e agora está na [yellow]página "
            f"{self.pagina_atual}[/]")
        if self.fim_do_livro():
            print(f":closed_book:[red] Você chegou ao final do livro "
                  f"'{self.titulo}'[/]")
                
    def fim_do_livro(self):
        return True if self.pagina_atual == self.total_paginas else False



livro1 = Livro("10 coisas que aprendi", 20)
livro1.avancar_paginas(5)
livro1.avancar_paginas(10)
livro1.avancar_paginas(50)
livro1.avancar_paginas(5)