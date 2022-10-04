if __name__ == '__main__':
    while True:
        try:
            num = int(input('Introduza um número: '))
            print('=' * 12)
            for j in range(1, 11):
                mult = j * num
                print(f'{num:2} x {j:2} = {mult}')
                j += 1
            break
        except ValueError:
            print('Introduza um número válido.')
    print('=' * 12)
