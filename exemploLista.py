if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        nome = input('Nome: ')
        nl = nome.split(' ')
        print(f'O nome tem {len(nl)} palavras.')
        print(nl[0])
        for j in nl:
            print(j)
        x = 0
        # while x < len(nl):

    print('Adeus!')
