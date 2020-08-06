# -*- coding: utf-8 -*-

print('==========================')
print('Calcule a média dos Alunos')
print('==========================')

nota_01 = int(input('Digite a nota 1'))
nota_02 = int(input('Digite a nota 2'))
nota_03 = int(input('Digite a nota 3'))
nota_04 = int(input('Digite a nota 4'))

media = (nota_01 + nota_02 + nota_03 + nota_04) / 4
if media >= 7:
    print('Você foi aprovado com a media de ' + str(media))
else:
    print('Você foi reprovado com a media de ' + str(media))
