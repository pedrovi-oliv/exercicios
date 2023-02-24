import math
y = float(input('Digite o valor do ângulo: '))
x = math.radians(y)
print('O cosseno de {} vale {:.2f}'.format(y, math.cos(x)))
print('O seno de {} vale {:.2f}'.format(y, math.sin(x)))
print('A tangente de {} vale {:.2f}'.format(y, math.tan(x)))
