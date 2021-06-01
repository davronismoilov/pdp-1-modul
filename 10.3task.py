'''
1- va 2- topshiriqda yozgan kodingizni try/except ichida yozib
, ekranga errorni chiqaradigan kod yozing
'''
try :
    a = [1, 5, 8, 5, 6, 5, 8, 5]
    print(a[9])

except IndexError as e:
    print(e)

try:
    ab = {'a': 12, "b": 3, 'c': 6}
    print(ab[45])
except KeyError :
    print('key error ishlayapti :')
try:
    a = 12
    b = 'salom Davron '
    print(int(a) + b)
except TypeError as e:
    print(e)
