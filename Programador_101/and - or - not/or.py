"""
Para o operador 'or'
Qualquer sentença verdadeira, as outras serão verdadeiras
Ou seja (ou um ou outro)
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
