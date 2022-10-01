if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        num1 = int(input('Introduza o primeiro número: '))
        num2 = int(input('Introduza o segundo número: '))
        if num1 > num2:
            print(f'O número {num1} é maior.')
        if num1 < num2:
            print(f'O número {num1} é menor.')
        else:
            print(f'O primeiro número {num1} é igual ao segundo número {num2}.')

        continuar = input('Pretende repetir? [s] ou [n]? ')
print(f'Adeus!')