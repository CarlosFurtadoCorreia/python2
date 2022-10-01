'''
Pedir o BI ao utilizador, nome, morada, codigo postal, custo hora xx.xx, ano nascimento xxxx
'''

if __name__ == '__main__':
    '''
    bi = input('Introduza o seu BI: ')
    nome = input('Introduza o seu nome: ')
    morada = input('Inroduza a sua morada: ')
    cod_postal = input('Introduza o seu código postal: ')
    custo_hora = input('Introduza o seu custo hora: ')
    ano_nasc = input('Introduza o seu Ano de Nascimento: ')

    print(f'BI: {bi} \n'
          f'Nome: {nome} \n'
          f'Morada: {morada} \n'
          f'Código Postal: {cod_postal} \n'
          f'Custo Hora: {custo_hora} \n'
          f'Ano Nascimento: {ano_nasc}')
    '''

    dados = ['bi', 'nome', 'morada', 'cod_postal', 'custo_hora', 'ano_nasc']
    for x in range(dados):
        dados[x] = input(f'Insira {dados[x]}')
        break
    print(dados)
