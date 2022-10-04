def calcs(num1, num2):
    num = 8
    st = ''
    for j in range(num1, num2):
        st += str(j)
        calc = int(st) * num + j
        print(f'{st} × {num} + {j} = {calc}')


if __name__ == '__main__':
    while True:
        nInicial = 1
        nFinal = 10

        calcs(nInicial, nFinal)

        continuar = input('Pretende repetir? [s] | [n]: ')
        if continuar == 'n':
            break
