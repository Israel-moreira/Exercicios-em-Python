from datetime import date
atual = date.today().year

def voto(nas):
    idade = atual - nas
    if idade >= 18 and idade <= 70:
        print(f'Com {idade} anos seu voto é OBRIGATÓRIO.')
        return nas
    if idade > 70:
        print(f'Com {idade} anos seu voto é OPCIONAL.')
        return nas
    if idade >= 16 and idade < 18:
        print(f'Com {idade} anos de idade seu voto é OPCIONAL.')
        return nas
    if idade < 16:
        print(f'Com {idade} anos, você ainda não tem o direito de votar.')
        return nas


nas = voto(int(input('Em qual ano você nasceu? ')))
