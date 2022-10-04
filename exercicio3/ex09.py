'''
9. Escreva um programa em Python que lê uma sequência de dígitos, sendo
cada um dos dígitos fornecido numa linha separada, e calcula o número
inteiro composto por esses dígitos, pela ordem fornecida. Para terminar a
sequência de dígitos é fornecido ao programa o inteiro
'''

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
