"""Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligini alifbo tartibida chiqaradigan dastur tuzing
Masalan:  Ismlar: john, alice, bob
  Natija: alice, bob, john"""

words = input("Vergul bilan ajratib so'zlar kiriting:\n Ismlar : ").split(sep=",")
words.sort()
print ('Natija : ')
for i in words :
    print(words[i],end=",")