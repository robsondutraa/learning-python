time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(1, tot + 1):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.').upper()
    if resp == 'N':
        break

print('-=-' *40)
print('Cod ', end='')

for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(time):
    print(f'{k + 1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (DIGITE 999 PARA ENCERRAR.) '))
    if busca == 999:
        break
    elif busca > len(time):
        print(f'ERRO! Não existe jogador com código {busca}! ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca - 1]["Nome"]}.')
        for i, g in enumerate(time[busca - 1]['Gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-=-' * 30)
print('<< VOLTE SEMPRE! >>')