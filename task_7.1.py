"""Standart input orqali vergul bilan ajratilgan sonlarni o'qing va
 u yerda nechta son qatnashganini ekranga chiqaring (takrorlanishlar inobatga olinmasin).

Misollar:
Input: 2,3,3,4
Natija: 3

Input: 1,1,1,1,1
Natija: 1

Input: 1,2,3
Natija: 3"""
my_set = set(map(int,input('vergul bilan sonni kiriting\n Input: ').split(sep =',')))
print(' Natija : ',len(my_set))