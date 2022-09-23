'''
Este programa implementa funções aritméticas
'''


def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1  # zeros = zeros + 1
    return zeros



if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        numero = int(input('Insira um número: '))
        print(f'Olá, o número {numero} tem {divisores(numero)} divisores')
        if divisores(numero) == 2:
            print(f'O número {numero} é primo.')
        else:
            print(f'O número {numero} não é primo.')
        continuar = input('Repetir [s] ou [n]? ')
    print('Adeus!')
