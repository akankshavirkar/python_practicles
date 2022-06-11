def digitsSum(Number):
    Sum = rem = 0
    while Number > 0:
        rem = Number % 10
        Sum = Sum + rem
        Number = Number // 10
    return Sum



Number = int(input("Enter the Number = "))
Sum = digitsSum(Number)

print("The Sum of the Digits = %d" %Sum)

if Number % Sum == 0:
    print("%d is a Harshad Number." %Number)
else:
    print("%d is Not." %Number)
