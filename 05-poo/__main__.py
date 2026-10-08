from jogorpg import *

def main():

    p1 = Guerreiro("Megaman", 1000)
    p2 = Mago("Merlin", 5000)

    p1.atacar(p2,200)
    p2.atacar(p1, 200)

    p1.curar()
    p2.curar()

if __name__ == "__main__":
    main()