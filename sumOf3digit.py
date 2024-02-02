print("program that will give you the sum of 3 digits")
num=int(input("Enter #3 digit number "))

# input 123
val1=num%10  #3
val2=num//10  #12
val3=val2%10  #2
val4=val2//10  #1
print(val2) #if enter 1 so 1/10 ==roundoff return 0


# print(val1+val3+val4)


# def sumOfDigit(n):
#     sum=0
#     for i in str(n):
#         sum+=int(i)
#     return sum

# sum=sumOfDigit(num)
# print(sum)


# def sumofDigits(n):
#     sum=0
#     while (n!=0):
#         sum=sum+(n%10)
#         n=n//10   #it will give whole divisible number
#     return sum

# ans=sumofDigits(num)
# print(ans) 


