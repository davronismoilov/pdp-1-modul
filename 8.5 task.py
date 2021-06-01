'''
Parametr sifatida ismni
o’qib olib, uni teskari tartibda
 chiqarib beradigan funksiya tuzing.
'''
def rename (name):
    return name[::-1]
name = input("Ismni kiriting : ")
print(rename(name).capitalize())