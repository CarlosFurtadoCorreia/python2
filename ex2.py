if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        for j in range(1, 11):
            for k in range(1, 6):
                print(f'j= {j} y={k}')
        # print(f'{j} e o {k}')
        continuar = input('Repetir [s] ou [n]? ')
    print('Adeus!')
