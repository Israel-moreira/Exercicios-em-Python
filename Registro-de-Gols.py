dados = {}
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
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
