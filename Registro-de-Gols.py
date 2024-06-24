time = []
dados = {}
while True:
    dados.clear()
    jogador = dados['Jogador'] = str(input('Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador} jogou? '))
    golsporpartida = []
    tot = 0
    if partidas > 0:
        for c in range(0, partidas):
            gols = int(input(f'Quantos gols na partida {c+1}: '))
            golsporpartida.append(gols)
            tot += gols
    else:
        dados['Gols'] = 0
    dados['Gols'] = golsporpartida
    dados['Total'] = tot
    time.append(dados.copy())
    while True: 
        resp = str(input('Quer continuar [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-~' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-~' * 30)