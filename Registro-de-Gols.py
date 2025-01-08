time = []
dados = {}

def lin():
    print('-' * 60)

while True:
    dados.clear()
    jogador = input('Jogador: ').strip()
    partidas = int(input(f'Quantas partidas {jogador} jogou? '))
    golsporpartida = []
    tot = 0
    
    if partidas > 0:
        for c in range(1, partidas + 1):
            gols = int(input(f'Quantos gols na partida {c}: '))
            golsporpartida.append(gols)
            tot += gols
    dados['Jogador'] = jogador
    dados['Gols'] = golsporpartida if partidas > 0 else [0]
    dados['Total'] = tot
    
    time.append(dados.copy())
    
    while True: 
        resp = input('Quer continuar [S/N]? ').strip().upper()
        if resp in ['S', 'N']:
            break
        print('ERRO! Responda apenas S ou N.')

    if resp == 'N':
        break

lin()
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
lin()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
lin()
