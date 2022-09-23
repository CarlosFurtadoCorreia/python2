'''
EXERCÍCIO
'''


def get_letras(nota):
    letra = 'E'
    if nota > 80:
        letra = 'A'
    if nota >= 60:
        letra = 'B'
    if nota >= 40:
        letra = 'C'
    if nota >= 20:
        letra = 'D'
    if nota >= 0:
        return 'E'

    return letra


if __name__ == '__main__':
    while True:
        nota = int(input('Insira a nota: '))
        print(f'O numero {get_letras} é par.')
        continuar = input('Repetir [s] ou [n]? ')
        if continuar == 'n':
            break
    print(f'Adeus!')
