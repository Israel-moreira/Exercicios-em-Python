colaboradores = []
pessoa = {}
media = soma = 0

def lin():
    print('-=' * 30)

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').strip()
    
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    colaboradores.append(pessoa.copy())
    
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    
    if resp == 'N':
        break

lin()
print(f'Ao todo temos {len(colaboradores)} colaboradores cadastrados.')
media = soma / len(colaboradores)
lin()
print(f'A média de idade dos colaboradores cadastrados é: {media:5.2f} anos')

# Mulheres cadastradas
print('As mulheres cadastradas são: ', end='')
for p in colaboradores:
    if p['sexo'] == 'F':
        print(f'({p["nome"]}) ', end='')
print()

lin()

# Colaboradores acima da média de idade
print('Lista de colaboradores que estão acima da média de idade: ', end='')
for p in colaboradores:
    if p['idade'] >= media:
        print(f'({p["nome"]}) ', end='')
print()

print('<<< Encerrado >>>')
