'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
Input: n = 3
Output: ["1","2","Fizz"]
'''
n=int(input('n = '))
a= []
for i in range (1,n+1):
    if i%3 == 0 and i%5==0:
        a.append("FizzBuzz")
    elif i % 3 == 0:
        a.append("Fizz")
    elif  i%5 == 0:
        a.append("Buzz")
    else :
        a.append(i)



print(a)