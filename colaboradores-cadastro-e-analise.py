colaboradores = []
pessoa = {}
media = soma = 0

def lin():
    print('-=' * 30)


while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    colaboradores.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N ')
    if resp == 'N':
        break
lin()
print(f'Ao todo temos {len(colaboradores)} colaboradores cadastradas.')
media = soma / len(colaboradores)
lin()
print(f'A média de idades dos colaboradores cadastradas é: {media:5.2f} anos')
print(f'As mulheres cadastradas são: ', end='')
for p in colaboradores:
    if p['sexo'] in 'Ff':
        print(f'({p['nome']}) ', end='')
print()
lin()
print('Lista de colaboradores que estão acima da média de idade: ', end='')
for p in colaboradores:
    if p['idade'] >= media:
        print(f'({p['nome']}) ', end='')
print()
print('<<< Encerrado >>>')
