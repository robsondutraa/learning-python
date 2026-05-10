print('Digite um número para')
num = int(input(('cálcular sua fatorial: ')))
fatorial = num #Inicialização de váriavel que já começa com o valor digitado pelo usuário.
produto = 1 #inicialização de variavel
multiplicadores = '' #Uma String vazia para armazenas as strings de fatorial

while fatorial >= 1: # Toda multiplicação tem que ser iniciada com 1
     produto *= fatorial # Aqui é feita a atualização da multiplicação e multiplicando pelo valor atual de fatorial, isso vai acumulando o resultado de fatoria.
     multiplicadores += str(fatorial) + ' x ' #Aqui é feito a criação de uma string que transforma fatorial em uma string e é adicionado x para cada string adiconada, exemplo 5 x 4 x. Sempre que vier um número que no caso está em forma de string.
     fatorial -= 1 #Aqui é feita a subtração do valor de fatorial, para que seja feito isto... 5 x 4 x 3 x 2 x 1, cade repetição ele diminui um, assim sucessivamente.
multiplicadores = multiplicadores[:-3] #Aqui é só pra tirar 3 caracteres do final do texto
print('O fatorial de {}! = {} = {}'.format(num, multiplicadores, produto))
