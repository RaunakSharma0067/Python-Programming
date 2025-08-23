def sumValue(*n):
    sum = 0
    for i in n:
        sum = sum + i
    print("sum=", sum)

sumValue(10, 20)
sumValue(10.23, 20.10)
sumValue(10, 20, 30)
sumValue(10)
sumValue()



