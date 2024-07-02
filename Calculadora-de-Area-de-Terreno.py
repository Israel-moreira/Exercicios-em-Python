# Projeto: Calculadora de Área de Terreno

def area(largura, comprimento):
    print('-=' * 39)
    print(f'A área do seu terreno é: {largura * comprimento:.2f} M²')
    print('-=' * 39)

def intro():
        print('-=' * 39)
        print(f'{"CALCULADORA DE TERRENO - v1":^39}')
        print('-=' * 39)

intro()
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area(largura, comprimento)
