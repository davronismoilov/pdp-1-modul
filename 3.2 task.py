"""Dasturingizni yangilang:
 kiritilgan ma'lumotni birinchi belgisini
  katta harf ko'rinishida qolganlarini kichik harf
  ko'rinishida qoladigan bo'lsin va dasturingiz familyangiz bilan
   ham ishlay oladimi?"""
name=input("Ismingizni kiriting ")
sur_name=input("Familyangizni kiriting ")

about=f"Assalomu alaykum {name.capitalize()} {sur_name.capitalize()} dasturga xush kelibsiz!"
print(about)