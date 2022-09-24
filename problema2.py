'''
2. Pede ao utilizador um numero inicial. Pede ao utilizador
    um numero que representa "Quantos" mostra aquela quantidade
    de numeros primos a partir do numero inicial
'''


if __name__ == '__main__':
    primos = 0
    continuar = 's'
    while continuar == 's':
        num1 = int(input('Insira um número: '))
        quantos = int(input('Insira quantos números primos pretende verificar: '))
        quantidade = 0
        while quantidade <= quantos:
            for j in range(num1, quantos + 1):
                if j >= 1:
                    for k in range(2, j):
                        if j % k == 0:
                            break
                    else:
                        print(j)
                        primos += 1
                        quantidade += 1
            break
        continuar = input('Repetir [s] ou [n]? ')
    print('Adeus!')
