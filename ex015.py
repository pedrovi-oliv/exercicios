km = float(input('Quantos quilômetros foram rodados?: '))
d = float(input('Quantos dias você usou o carro?: '))
# 60 por dia e 0,15 por km rodado
p = (km*0.15)+(d*60)
print('O total a pagar é: R${:.2f}'.format(p))
