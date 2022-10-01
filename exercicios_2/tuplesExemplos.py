#Exemplo de tupple (com dados e dicionário(titulo e resposta))
pessoa = (1, 'Maria', {'morada': 'Rua de Cima,1', 'cp': 9500}, 12.50)

#Exemplo de set
meses = {'Março', 'Fevereiro', 'Janeiro'}

if __name__ == '__main__':
    #.keys imprime os titulos
    print(pessoa[2].keys())
    #.values imprime as repostas aos titulos
    print(pessoa[2].values())
    print()
    for k in pessoa[2].keys():
        print(k)
    for j in pessoa[2].values():
        print(j)
    print()
    for k in pessoa[2].keys():
        print(f'{k} = {pessoa[2][k]}')
    print(meses)
    #adicionar dado ao set
    meses.add('Abril')
    meses.add('Abril')
    print(meses)
    #não deixa duplicar os dados do set
    meses.pop()
    print(meses)
