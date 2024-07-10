import moeda

valor = float(input('Digite um valor: R$'))
print(f'O dobro de R${valor:.2f} é R${moeda.dobro(valor):.2f}')
print(f'A metade de R${valor:.2f} é R${moeda.metade(valor):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor, 10):.2f}')
print(f'Reduzindo 13%, temos R${moeda.diminuir(valor, 13):.2f}')