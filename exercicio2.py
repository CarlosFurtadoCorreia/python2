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
        print(f'A frase tem o comprimento de {len(frase)}.')
        #print(f'')
        fl = frase.split(' ')
        continuar = input('Repetir [s] ou [n]? ')
    print('Adeus!')