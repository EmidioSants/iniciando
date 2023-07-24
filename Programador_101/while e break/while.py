
"""
Repetição
 while (enquanto)
 Executa uma ação enquanto uma condição for verdadeira
"""

contador = 0

while contador < 50:
    contador += 1

    if contador == 15:
        print('Engoli o 15')
        continue

    if contador >= 20 and contador <= 30:
        print('Roubei 10')
        continue

    print(contador)

    if contador == 49:
        break

print('Fim!')