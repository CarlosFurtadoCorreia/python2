'''EXERCÍCIO 3

- Pedir ao utilizador para escrever uma frase com + de 10 caracteres
- Não permitir mais que 2 caracteres seguidos iguais
- Quantas unidades de caracteres de cada contém a frase
- Frase tem que terminar obrigatoriamente com '. ! ?'''

if __name__ == '__main__':
    count_frase = 0
    final_frase = ['.', '!', '?']

    while count_frase < 10:
        frase = input('Insira uma frase com mais de 10 caracteres. (Deve terminar com ". ! ?"): ')
        count_frase = len(frase)
        x = count_frase - 1
        if count_frase < 10:
            print('A frase deve ter mais de 10 caracteres.')

        if frase[x] in final_frase:
            pass
        else:
            print('A frase deve terminar com ". ! ?"')
            x = 0

        check_char1 = 0
        check_char2 = 0
        check_char3 = 0

        for j in range(0, len(frase)):
            if j + 2 < len(frase):
                check_char1 = frase[j]
                check_char2 = frase[j + 1]
                check_char3 = frase[j + 2]
                if check_char1 == check_char2 and check_char1 == check_char3:
                    print(f'A frase não pode ter mais que 2 caracteres repetidos seguidos.'
                          f'({check_char1}'
                          f'{check_char2}'
                          f'{check_char3})')
        print(f'{frase}')

        '''for j in range(1, len(frase)):
            if check_char == frase[j]:
                print('A frase não pode ter mais que 2 caracteres repetidos seguidos.')
                x = 0
                break
            check_char = frase[j]
        print(frase)'''