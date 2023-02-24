a = float(input('Digite a largura da sua parede: '))
b = float(input('Digite a altura da sua parede: '))
area = a*b
baldes = area/2
print('Sua parede tem dimensão de {}X{}m² e irá necessecitar de {} baldes de tintas'.format(int(a), int(b), baldes))
