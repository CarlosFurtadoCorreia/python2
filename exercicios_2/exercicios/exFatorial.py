#EXERCICIO PARA CALCULAR O FATORIAL INTRODUZIDO

if __name__ == '__main__':

    num = int(input('Introduza um número: '))
    fim = 1
    count = 1

    '''while count <= num:
        fim *= count
        count += 1
    '''

    for x in range(num):
        fim *= count
        count += 1
    print(fim)
