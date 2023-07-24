"""
Fatiamento de strings

012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs .: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

print(variavel[2]) # retorna a posição do caracter
print(len(variavel)) # retorna a quantidade de caracter
print(variavel[4:]) #fatia a variável de acordo com o determinado em colchetes [inicio: fim: step]
print(numeros[0:15:3])
print(numeros[::])#exibe tudo

