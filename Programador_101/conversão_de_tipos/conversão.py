#Conversão de tipos, coerção
#type conversion, typecasting, coercion
#é o ato de converter um tipo em outro tipo imutáveis e primiitvo:
#str, int, float, bool


print(int('1'), type(int('1')))
print(type(float('1')+1))
print(bool('')) #um boolean vazio será dado como False - 0
print(bool(' '))#um boolean com algum dado, até mesmo um espaço, será dado como True - 1
print(str(11) + 'b')