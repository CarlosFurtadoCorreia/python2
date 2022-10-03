'''
8. Escreva um programa em Python que lê o número de horas, que um em-
pregado trabalhou numa dada semana e o seu salário/hora e calcula o
ordenado semanal tendo em conta as horas extraordinárias. O salário é
calculado do seguinte modo: se o número de horas fôr menor que 40 então
salário é dado pelo produto do número de horas pelo salário hora, em caso
contrário recebe horas extraordinárias as quais são pagas a dobrar.
'''

if __name__ == '__main__':
    semana = ['Segunda-feira', 'Terça-feira',
                 'Quarta-feira', 'Quinta-feira',
                 'Sexta-feira', 'Sábado', 'Domingo']
    num_horas = []
    total_horas = 0
    for j in range(len(semana)):
        num_horas.append(int(input(f'Introduza o {semana[j]}: ')))
        total_horas += num_horas[j]
    sal_hora = int(input(f'Introduza o seu salário por hora: '))
    salario = sal_hora * total_horas
    if total_horas < 40:
        salario
    else:
        salario * 2

    print(num_horas)
    print(sal_hora)
    print(total_horas)
    print(salario)


