# Write a program that will take three digits from the user and add the square of each digit.

val=123

a=val%10
val=val//10

b=val%10
val=val//10

c=val%10
val=val//10

print(c**2+b**2+a**2)


def sqOfDigits(n):
    val=0
    while(n!=0):
        sqr=(n%10)**2
        val=val+sqr
        n=n//10
    return val

val2=sqOfDigits(12345)
print(val2)


