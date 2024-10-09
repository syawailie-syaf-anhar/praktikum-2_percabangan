number = int(input("Enter a number:"))
if(number%2==0):
    print("number is even")
else:
    print("number is Odd")
print("\n===========")

score = int(input("Enter your test score (0-100) : "))

if 90 <= score <= 100 :
    print("Very good")
elif  80 <= score <= 89:
    print("Good")
elif 70 <= score <= 79 :
    print("Fair")
elif 60 <= score <= 69:
    print("poor")
else:
    score < 60
    print("very poor")
print("\n==========")

age = int(input("Enter your age : "))
blood = int(input("Enter your blood pressure : "))

if age >= 60 and blood > 140 :
    print("High")
elif age >= 60 and blood <= 140 :
    print("Normal")
elif age < 60 and blood > 130 :
    print("High")
elif age < 60 and blood <= 130 :
    print("Normal")
else:
    print("Not Defined")