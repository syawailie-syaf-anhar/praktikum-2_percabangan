#Paraktikum 2 Alpro 

#menentukan apakah sebuah angka itu ganjl atau genap
number = int(input("input a number: "))
if(number%2==0):
    print(f"number {number} is even")
else:
    print("number is Odd")
print("\n==========================")

#menentukan rance nilai 
score = int(input("imput your test score (0-100) : "))

if 90 <= score <= 100 :
    print("your score is very good")
elif  80 <= score <= 89:
    print("your score is good")
elif 70 <= score <= 79 :
    print("your score is Fair")
elif 60 <= score <= 69:
    print("your score is poor")
else:
    score < 60
    print("your score is very poor")
print("\n========================")

#menentukan status kesehatan berdasarkan umur dan tekanan darah
age = int(input("input your age : "))
blood = int(input("input your blood pressure : "))

if age >= 60 and blood > 140 :
    print("Health Status is High")
elif age >= 60 and blood <= 140 :
    print("Health Status is Normal")
elif age < 60 and blood > 130 :
    print("Health Status is High")
elif age < 60 and blood <= 130 :
    print("Health Status is Normal")
else:
    print("Not Defined")
