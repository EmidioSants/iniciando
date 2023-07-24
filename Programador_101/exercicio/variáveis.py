nome = input('Digite seu nome: ')
idade = input('Digite dua idade: ')

if nome and idade:
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome possui espaço')
    else:
        print('Seu nome NÃO possui espaço')

    print(f'Seu nome possui {(len(nome))} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Você não digitou nada!')