'''
Exercício para descobrir se o numero é par ou nao
'''


def par(numero):
    resto = numero % 2
    if resto == 0:
        return True
    if resto != 0:
        return False
    '''
        else:
            return False
    '''


if __name__ == '__main__':
    while True:
        num = int(input('Insira um numero: '))
        if par(num):
            print(f'O numero {num} é par.')
        else:
            print(f'O numero {num} é impar.')
        continuar = input('Repetir [s] ou [n]? ')
        if continuar == 'n':
            break
    print(f'Adeus!')
