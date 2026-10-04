print("===== student system =====")
name=input("enter your name: ")
age=input("enter your age: ")
grade=input("enter your grade: ")

print("hello " + name)
print("your age is:"+age)
print("your grade is:"+grade)
if grade >"50":
 print("good")
else:
 print("not good")
print("===== Calculator=====")
firstnumber=int(input("enter first number:"))
opreator=input("enter opreator")
secondnumber=int(input("enter second number"))

result=firstnumber + secondnumber,
firstnumber - secondnumber,
firstnumber * secondnumber,
firstnumber / secondnumber
print( "result is" , result)

if opreator == "+":
 print(firstnumber + secondnumber)
elif opreator == "-":
 print(firstnumber - secondnumber)
elif opreator =="*":
 print(firstnumber * secondnumber)
elif opreator == "/":
 print(firstnumber / secondnumber)
else:
 print("invalid opreator")

print("===== student id generator =====")
num=int(input("enter a number "))
for i in range(1,num + 1,):
 print(i)