"""2-topshiriq

Standar input orqali son qabul qiling,
agar bu son 3ga qoldiqsiz bo'linsa ekranga "Fiz",
5ga qoldiqsiz bo'linsa "Biz", ham 5ga ham 3ga qoldiqsiz bo'linsa "FizBiz" ni ekranga chiqaring.
Agar son hech qaysi shartni bajarmasa sonni o'zini ekranga chiqaring.

Misollar:
Input: 3
Natija: Fiz

Input: 10
Natija: Biz

Input: 15
Natija: FizBiz

Input: 17
Natija: 17"""
number=int(input("Input: "))
if number%3==0 and number%5==0:
    print("Natija: FizBiz")
elif number%3==0 :
    print("Natija: Fiz")
elif number%5==0 :
    print("Natija: Biz")
else :
    print(f"Natija: {str(number)}")