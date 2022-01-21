def fact(a):
    f = 1
    for i in range(1,a+1):
        f = f * i
    return (f)

x = 5
y = 3
num1 = fact(x-y)
num2 = fact(x)
print(num2/num1)
