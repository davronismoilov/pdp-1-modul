"""Standart kiruvchi ma'lumot sifatida ikkita so'zni o'qib olib,
ularning anagram (bitta so'zni ikkinchisidan ajratib olish mumkin)
ekanligini tekshiruvchi dastur tuzing. Havola: https://leetcode.com/problems/valid-anagram/
Masalan:
Kiruvchi ma'lumot: anagram gramana
Natija: True
Kiruvchi ma'lumot: rat cat
Natija: False"""
a = (input(' Input: ').split())

c = set(a[0])
d = set(a[1])
# d to'plamda a mavjud bo'lsa True qaytadi

print(' Natija :',c.issubset(d))