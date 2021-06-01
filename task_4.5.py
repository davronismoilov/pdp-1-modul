"""Foydalanuvchidan haqiqiy son so’rab uni
 ilmiy ko’rinishga o’tkazib chiqaradigan dastur tuzing.
Masalan: 120000—>1.2*10^5"""

a=float(input("a="))
n=a
s=0
while a>0:
    s+=1
    a//=10
print(str(n/10**(s-1))+"*10^"+str(s-1))