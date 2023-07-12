#Primeira aula de Python, apresentação da IDE e Interpretador Python

titulo = "Interpretador"
nome = "Emidio"
sobrenome = "Santos"
idade = 2023 - 1992
ide = "Intellij"
versao = "Python Versão 3.11"

print(f'{titulo:*^50}\n'
    f'Nome: {nome} \n'
    f'Sobrenome: {sobrenome} \n'
    f'Idade: {idade} \n'
    f'{ide}'
    f'{versao}')

#Docstring
"""
Um comentário em Python é feito com o uso do simbolo "#"

Quando usa-se aspas tríplas não se trata de um comentário mas sim de um Docstring,
que é lido pela linguagem
"""