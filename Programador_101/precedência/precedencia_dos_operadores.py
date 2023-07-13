# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5 # 7 (resultado errado)
conta_2 = (1 + 1) ** (5 + 5) # 1024 (correta com a ordem de precedencia
print(f'{conta_1}\n'
    f'{conta_2}')