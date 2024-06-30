def fatorial(num=1, show=False):
    """
    -> fatorial(num, show=False)
    :param num: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor fatorial de um número (num).
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c}', end=' = ')
    return f

num = int(input('Digite um número: '))
show = str(input('Gostaria de ver o cálculo? [S/N] ')).upper()[0]
if show == 'S':
    show = True
else:
    show = False
print(fatorial(num, show))
