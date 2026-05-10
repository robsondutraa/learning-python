divisão = 0 
num = int(input('Digite um número: '))
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[33m', end=' ')
        divisão += 1
    else:
        print('\033[31m', end=' ')
    print(cont, end='\033[m')
print('\033[m\nO número {} foi divisivel em {} vezes.'.format(num, cont))

if divisão == 2:
    print('E por isso ele É PRIMO!'.format(num))
else: 
    print('E por isso ele NÃO É PRIMO!'.format(num))


    