total_pessoa = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')

    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    total_pessoa.append(pessoa.copy())

    while True:
        resp = input('Quer continuar? [S/N] ').upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if resp == 'N':
        break

print('-=-' * 30)
print(f'A) Ao todo temos {len(total_pessoa)} pessoas cadastradas')

media = soma / len(total_pessoa)
print(f'B) A media de idade é de {media:5.2f} anos')

print(f'C) As mulheres cadastradas foram ', end='')
for p in total_pessoa:
    if p['sexo'] in'Ff':
        print(f'{p["nome"]}', end='')
print()

print('D) Lista de pessoas que estão acima da média: ')
for p in total_pessoa:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
        
print(' << ENCERRADO >>')   
