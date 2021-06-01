
'''
Standart kirituvchi ma’lumot sifatida ismlarni
o’qib olib, ularning ichidan eng uzunini chiqaruvchi dastur tuzing
'''
def maxname(a):
    max = 0
    for i in range (len (a)):
        if len(a[i]) >=len(a[max]) :
            max = i

    return print(f'kiritilgan ismlar orasida eng kattasi: -- {a[ max]}')
a=list(input('ismlarni kiriting : ').split(" "))
maxname(a)