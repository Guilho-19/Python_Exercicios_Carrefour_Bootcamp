# -*- coding: utf-8 -*-

menu = int(input('1 - Netflix | 2 - Amazon Prime | 3 - Sair'))

def opcao1():
    print('Abrindo Netflix...')
def opcao2():
    print('Abrindo Amazon Prime...')
def opcao3():
    print('Saindo...')

opcoes = { 1:opcao1, 2:opcao2, 3:opcao3}

if menu == 1:
    opcoes.get(1)()
if menu == 2:
    opcoes.get(2)()
if menu == 3:
    opcoes.get(3)()
