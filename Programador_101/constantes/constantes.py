"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
"""

velocidade = 60 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR1 = 60 # velocidade máxima do radar 1
LOCAL1 = 100 # local onde o radar 1 está
RADAR_RANGER = 1 # A distância onde o radar pega

if velocidade >= RADAR1 and local_carro >= LOCAL1:
    print('Carro acima da velocidade, MULTADO')
if velocidade <= RADAR1 and local_carro <= LOCAL1:
    print('Carro dentro da velocidade, NÃO MULTADO')
