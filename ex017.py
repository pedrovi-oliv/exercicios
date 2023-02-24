from math import sqrt
a = float(input('Digite o valor do cateto adjacente: '))
o = float(input('Digite o valor do cateto oposto: '))
h = sqrt(a**2+o**2)
print('a hipotenusa mede= {:.2f}'.format(h))
