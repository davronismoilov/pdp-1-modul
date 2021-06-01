"""Standart input orqali olingan son toq yoki juft ekanligini ekranga chiqaring.
Misollar:
Input: 3
Natija: 3 - toq son

Input: 18
Natija: 18 - juft son"""
number=int(input("Input: "))
if number%2==0 :
    print(f"Natija: {str(number)} - juft son")
else :
    print(f"Natija: {str(number)} - toq son")