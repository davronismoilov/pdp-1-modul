"""Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligida maqsad qilingan so'z necha marta takrorlanganligini aniqlovchi dastur tuzing
Masalan: -  Ismlar: alice, john, bob, alice, bob, john, alice
-  Maqsad: alice
-  Natija: 3"""

words = input("Vergul bilan ajratib so'zlar kiriting: ").split(sep=",")
a=input('Maqsad : ')
print('Natija : ',words.count(a))