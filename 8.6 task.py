
'''
Standart kiruvchi ma’lumot sifatida ismni o’qib olib,
 uni rekursiv funksiya yordamida teskari tartibda qaytaruvchi dastur tuzing
'''
def rec(a):
    if len(a)==1:
        print(a)
    else:
        print(a[-1],end="")
        rec(a[:-1])

name=input("ismni kiriting : ")

print(rec(name))