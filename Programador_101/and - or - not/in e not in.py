"""
Operadores in e not in
Strings são interaveis
0 1 2 3 4 5
e m i d i o
-6-5-4-3-2-1

-----------------------

nome = "emidio"

print('i' in nome)
"""

nome = input('Digite o nome: ')
trecho = input('Digite o trecho que deseja: ')

if trecho in nome:
    print(trecho)
else:
    print('Nada encontrado')