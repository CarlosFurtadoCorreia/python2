'''
EXERCÍCIO
'''


def notas(nota):
    if nota > 80:
        return 'A'
    if nota >= 60:
        return 'B'
    if nota >= 40:
        return 'C'
    if nota >= 20:
        return 'D'
    if nota >= 0:
        return 'E'


if __name__ == '__main__':
    while True:
        nota = int(input('Insira a nota: '))
        continuar = input('Repetir [s] ou [n]? ')
        if continuar == 'n':
            break
    print(f'Adeus!')

'''
    if nota >79:
        print("Sua nota corresponde a A")
    if nota <80 >59:
        print("Sua nota corresponde a B")
    if nota <60 >39:
        print("Sua nota corresponde a C")
    if nota <40 >19:
        print("Sua nota corresponde a D")
    if nota <20 >=0:
        print("Sua nota corresponde a E")
        continuar = input('Repetir [s] ou [n]? ')
        if continuar == 'n':
            break
    print("Adeus!")
'''
