primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')


if primeiro_valor == segundo_valor:
    print(f'Os valores são iguais: {primeiro_valor} e {segundo_valor}')
elif primeiro_valor > segundo_valor:
    print(f'O primeiro valor é maior: {primeiro_valor}')
elif primeiro_valor < segundo_valor:
    print(f'O segundo valor é maior: {segundo_valor}')
else:
    print('Nenhum valor informado')
print('Fora do sistema')
