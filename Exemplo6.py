"""
Faça um programa que permita ao usuário digitar o valor unitário e a quantidade de um produto
a ao final informar o valor a paga.
"""

valorunitario = float(input('Digite o valor: '))
quantidade = int(input('Digite a quantidade: '))
valortotal = valorunitario * quantidade
print('O valor total é:', float(valortotal),'R$')