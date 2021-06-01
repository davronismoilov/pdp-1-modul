'''
Standart kirituvchi ma’lumot sifatida ismlarni
o’qib olib, ularning ichidan eng kaltasini chiqaruvchi dastur tuzing
'''
def minname(a):
    min = 0
    for i in range (len (a)):
        if len(a[min])>=len(a[i]):
            min = i
    return print(f'kiritilgan ismlar orasida eng kichigi : {a[min]}')
a=list(input('ismlarni kiriting : ').split(" "))
minname(a)