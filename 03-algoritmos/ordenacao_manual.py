#Código para colocar uma list em ordem sem utilizar o sort(), isto é bastante usado em ESTRUTURA DE DADOS, como. Buble Sort, Select Sort, Insert Sort

valores = []
for i in range(0, 5): #Aqui criamos um loop de 5 repetições.

    num = int(input(f'Digite o valor: '))
    if i == 0 or num > valores[-1]: #Aqui é a parte principal, 
                                    #onde é feito a verificação para saber se o número se encotra na primeira posição
                                    #( num == 0 ) ou se ele se encontra na última posição (list[-1])
        valores.append(num) #Se for verdadeiro adicionamos o valor a lista.
        print('Adicionado ao final da lista...')
    else:
        posição = 0
        while posição < len(valores): #Aqui é a parte mais complexa que é saber se o número se encontra no meio da lista
                                      #Enquanto a posição ela for menor do que a quantidade de itens de valores a repetição vai continuar
            if num <= valores[posição]:# Se o número ele for <= aos valores na lista na posição em que ele se encontra
                                       #Exemplo, ele vai verificar se na posição 1, ele é maior que o elemento que está nesta posição
                                       #Se for maior é adicionado na posição do antigo número, utilizando o INSERT.
                valores.insert(posição, num) #Adicona na posição que ele estava
                print(f'O valor foi adicionado na posição {posição} da lista... ')
                break
            posição += 1 #Contador básico

print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}') #Print pra mostrar a lista em ordem


