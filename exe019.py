# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:07:47 2021

@author: Inayara
"""

'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela 
o nome do escolhido.'''

import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
print(f'O aluno sorteado é {random.choice(lista)}')




