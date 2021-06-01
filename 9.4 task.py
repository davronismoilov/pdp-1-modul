
'''
Standart kiruvchi ma’lumotdan sonlarni o’qib olib,
 ushbu sonlarning raqamlarini teskari tartibda chiqaruvchi dastur tuzing.
 Masalan:
Sonlar: 102 346 5897
Natija: 201 643 7985
'''
a=list(input("Sonlar: ").split(" "))
print('Natija',end=": ")
for i in range (len (a)):
    print(a[i][::-1],end=" ")
