listatemp = []
listaprin = []
maior = menor = 0
while True:
    listatemp.append(str(input('Digite o seu nome: '))) #Aqui vamos armazenar os valores nas listas
    listatemp.append(float(input('Digite o seu peso em (KG):')))
    if len(listaprin) == 0: #Verificação para pegar todo os valores da lista principal e ver se os elementos  são igual a 0, ou seja, se já inicou.
        maior = menor = listatemp[1] #Se não iniciou todos os elementos recebem a lista
    else:
        if listatemp[1] > maior: #Senão se, a lista temporária for maior do que o maior elemento, então maior = a lista temporária
            maior = listatemp[1]

        if listatemp[1] < menor: #Senão se, a lista temporária for menor do que o menor elemento, eentão o menor = a lista temporária
            menor = listatemp[1]
    listaprin.append(listatemp[:]) #Jogamos os valores pra lista principal
    listatemp.clear() #Limpa a antiga lista, ou seja, lista temporária
    resp = str(input('Você quer continuar, [S/N]? ')).strip().upper()
    if resp in 'N':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(listaprin)} pessoas.') #Diz a quantidade de pessoas
print(f'O maior peso foi de {maior}Kg. Peso de ', end='') #Diz o maior peso
for p in listaprin: #Onde é feito a verificaçaõ. Percorre toda a lista e verifica se o elemento na posição 1 ele é igual a váriavel maior, se for imprima ela.
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in listaprin: #Onde é feito a verificaçaõ Mas neste caso no menor número! Percorre toda a lista e verifica se o elemento na posição 1 ele é igual a váriavel maior, se for imprima ela.
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()

