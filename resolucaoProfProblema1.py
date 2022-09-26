def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1
    return zeros


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        ini = int(input('Insira o número inicial: '))
        fim = int(input('Insira o número final: '))
        k = ini
        primos = 0
        # Alterar o for para um while
        '''**FUNCINANDO** (PROF MANDOU SUBSTITUIR FOR POR WHILE)
        for n in range(ini, fim + 1):
            if divisores(n) == 2:
                print(n)
                primos += 1
        '''
        while k <= fim:
            if divisores(k) == 2:
                print(k)
                primos += 1
            k += 1
        print(f'Entre {ini} e {fim} há {primos} primos.')
        continuar = input('Repetir [s] ou [n]? ')
    print('Adeus!')
