"""Standart kiruvchi ma'lumotdagi vergullar bilan ajratilgan so'zlar ketma-ketligi orasida maqsad qilingan so'z aynan qaysi indeksda turganligini aniqlovchi dastur tuzing
Masalan:  -  Ismlar: john, alice, bob 
  Maqsad: bob
  Natija: 2"""

words = input("Vergul bilan ajratib so'zlar kiriting: ").split(sep=",")
a=input('Maqsad : ')
print('Natija : ',words.index(a))