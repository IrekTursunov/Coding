from random import randint
from time import time
x = randint(1, 2)
if x == 1:
    txt = 'солнце'
elif x==2:
    txt = 'амфибрахий'
print('Напишите данный текст: ', txt)
t1 = time()
txt1 = input()
t2 = time()
if txt1 == txt:
    print('Красавчик, все верно!')
    y = len(txt)
    velocity = *60(y//(t2-t1))
    print('y = ', y, 't2-t1 = ', t2-t1)
    print(velocity, ' - скорость вашей печати')
else:
    print('Неправильно :(')
