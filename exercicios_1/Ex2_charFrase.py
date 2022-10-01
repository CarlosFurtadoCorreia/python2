"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Qual é o comprimento da frase inserida (incluindo espaços)
 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""

if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        frase = input('Insira uma frase: ')
        print(f'A frase tem o comprimento de {len(frase)} caracteres.')
        fl = frase.split(' ')
        print(f'A frase contém {len(fl)} palavras.')
        cont_vogais = 0
        vogais = 'aeiouAEIOU'
        for v in frase:
            if v in vogais:
                cont_vogais += 1
        print(f'A sua frase tem {cont_vogais} vogais.')
        maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        minusculas = 'abcdefghijklmnopqrstuvwxyz'
        cont_maiusculas = 0
        cont_minusculas = 0
        for m in frase:
            if m != ' ':
                if m in maiusculas:
                    cont_maiusculas += 1
        print(f'A sua frase tem {cont_maiusculas} maiusculas.')
        for n in frase:
            if n != ' ':
                if n in minusculas:
                    cont_minusculas += 1
        print(f'A sua frase tem {cont_minusculas} minusculas.')
        nums = '0123456789'
        cont_nums = 0
        for o in frase:
            if o in nums:
                cont_nums += 1
        print(f'A sua frase tem {cont_nums} números.')
        print(f'{frase[::-1]}')
        continuar = input('Repetir [s] ou [n]? ')
    print('Adeus!')
