'''
1. Pede ao utilizador 2 numeros o 2º numero deve ser >= 1º
    mostra todos os numeros primos que há entre o 1º e o 2º,
    depois de mostrar os numeros diz quantos numeros primos
    havia.
'''

if __name__ == '__main__':
    primos = 0
    continuar = 's'
    while continuar == 's':
        num1 = int(input('Insira um primeiro número: '))
        num2 = int(input('Insira um segundo número (> que o primeiro numero): '))
        for j in range(num1, num2 + 1):
            if j > 1:
                for k in range(2, j):
                    if j % k == 0:
                        break
                else:
                    print(j)
                    primos += 1
        print(f'Entre o {num1} e o {num2} existem {primos} números primos.')
        continuar = input('Repetir [s] ou [n]? ')
    print('Adeus!')
