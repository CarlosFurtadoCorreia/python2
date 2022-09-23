'''
1. Pede ao utilizador 2 numeros o 2º numero deve ser >= 1º
    mostra todos os numeros primos que há entre o 1º e o 2º,
    depois de mostrar os numeros diz quantos numeros primos
     que havia.
'''

def primos(num1, num2):
    zeros = 0
    for n in range(num1, num2 + 1):
        if num2 % n == 0:
            zeros += 1  # zeros = zeros + 1
    return zeros


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        num1 = int(input('Insira um primeiro número: '))
        num2 = int(input('Insira um segundo número (> que o primeiro numero): '))
        print(f'{primos(num2)}')
        continuar = input('Repetir [s] ou [n]? ')
    print('Adeus!')