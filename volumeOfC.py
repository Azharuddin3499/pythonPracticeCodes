#  Write a program to find the volume of the cylinder. Also find the
# cost when ,when the cost of 1litre milk is 40Rs.


# volume=π r² h
r=4
h=7

volume=3.142*(r**2)*h
print(round(volume,2))
cost=(volume/1000)*40
print(round(cost,2))


