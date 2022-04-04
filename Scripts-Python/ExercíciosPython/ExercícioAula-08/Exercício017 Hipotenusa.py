import math
vNum1 = float(input('Digite o lado do cateto oposto:'))
vNum2 = int(input('Digite o lado do cateto adjacente:'))
vRes  = (math.hypot(vNum2,vNum2))
print ('A hipotenusa vai medir {:.2f}'.format(vRes))