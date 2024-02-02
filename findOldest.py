print("Find the Lasrget among 3 numbers")
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))

if num1 > num2 and num1>num3:
    print("%s is greater then %s and %s"%(num1,num2,num3))
elif num2 > num1 and num2> num3:
    print("%s is greater then %s and %s"%(num2,num1,num3))
else:
    print("%s is greater then %s and %s"%(num3,num2,num1))




