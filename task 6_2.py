"""Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligini teskari tartibda chiqaradigan dastur tuzing
Masalan:      Ismlar: john, alice, bob
                        Natija: bob, alice, john"""

words = input("Vergul bilan ajratib so'zlar kiriting:\n Ismlar: ").split(sep=",")
#First metod slise orqali chiqarish teskarisiga
print('Natija :',*words[::-1])
words.reverse()
print('Natija :',end=" ")
for i in range (len(words)):
    print(words[i],end=",")
