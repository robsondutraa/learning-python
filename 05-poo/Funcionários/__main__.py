from funcionarios import *

def main():
    func1 = FuncionarioHorista("Gabriel", 12, 200)
    func1.calc_sal()
    func1.analisar_sal()

    func2 = FuncionarioMensalista("Amanda", 9500)
    func2.calc_sal()
    func2.analisar_sal()

if __name__ == "__main__":
    main()