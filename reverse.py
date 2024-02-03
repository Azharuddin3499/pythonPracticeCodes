#Write a program that will reverse a four digit number.Also it checks
# In Python, strings are sequences of characters, and you can access individual characters or slices of characters using indexing and slicing.

# The syntax val[start:stop:step] is used for slicing, where:
# start is the starting index of the slice.
# stop is the ending index of the slice (exclusive).
# step is the step value, determining the increment between indices.

        # val='123456789'

        # print(val[2:9:2])

# for i in val[::-1]:
#     print(i)


val2=123456363252
print(str(val2)[::-1])



rev=1234
a=rev%10
rev=rev//10

b=rev%10
rev=rev//10

c=rev%10
rev=rev//10

d=rev%10
rev=rev//10

num=1000*a+100*b+10*c+d
print(num)

