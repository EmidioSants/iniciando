
"""
1
Faça um programa que peça ao usuário para digitar um número inteirio,
inform se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.

2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

saudacao = input("Olá, digite um numero inteiro: ")
try:
    hora = int(saudacao)
    if saudacao >= 0 and saudacao <= 11:
        print(f'São {saudacao} horas. Bom dia!!')
    elif saudacao >= 12 and saudacao <= 17:
        print(f'São {saudacao} horas. Boa tarde!!')
    elif saudacao >= 18 and saudacao <= 23:
        print(f'São {saudacao} horas. Boa Noite!!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor digite um numero inteiro')


"""

3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

nome = str(input('Informe seu nome: '))

if len(nome) <= 4:
    print('Seu nome é curto')
if len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
if len(nome) > 6:
    print('Seu nome é muito grande')
"""