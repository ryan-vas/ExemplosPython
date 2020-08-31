"""
Faça um programa que obtenha a partir da digitação do usuário os seguintes dados:
a quantidade de alunos que fazem o curso de sistemas de informação e a quantidade
de alunos que fazem o curso de análise de sistemas. Ao final o programa deve informar
o total de alunos, a porcentagem de alunos que fazem sistemas e a porcentagem de alunos
que cursam análises
"""

qtd_sistemas = int(input('Quantidade de alunos que cursam Sistemas: '))
qtd_análises = int(input('Quantidade de alunos que cursam Análises: '))
total_alunos = qtd_sistemas+qtd_análises
perc_sistemas = qtd_sistemas/total_alunos*100
perc_análises = qtd_análises/total_alunos*100
print('Total de alunos:', total_alunos)
print('Percentual de alunos que cursam Sistemas:', perc_sistemas,'%')
print('Percentual de alunos que cursam Análises:', perc_análises,'%')
