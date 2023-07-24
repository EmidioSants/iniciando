"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_floar = float(numero_str)
    print('Float:', numero_floar)
    print(f'O dobro de {numero_str} é {numero_floar * 2:.0f}')
except:
    print('Isso não é um numero')

