'''
15. Escreva um programa que lê uma série de dígitos (terminando com -1) e
calcula o inteiro que tem esses dígitos. Por exemplo, lendo os dígitos 1 5
4 5 8 -1, calcula o número inteiro 15458.
'''

def soma(n):
    num = 0
    for j in str(n):
        num += int(j)
    return num

if __name__ == '__main__':
    digitos = []

    while True:
        try:
            num = int(input('Introduza um dígito:\n'
                            '(-1 para terminar)\n'
                            f'? '))
            if num == -1:
                break
            digitos.append(num)

        except ValueError:
            print('Introduza um número válido.')
    num = ''
    for j in range(len(digitos)):
        num += str(digitos[j])

    print(f'O número é: {num}')
    print(f'O cálculo do número é {soma(num)}')