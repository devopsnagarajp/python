

a = 0
b = 1
f = [0,1]

def Fibonacci(n):
    while True:
    #for i in range(n-2):
        global a
        global b
        c = a + b
        if c < 100:
            f.append(c)
            a = b
            b = c
        else:
            print("Loop is broken.")
            break
    return b

#n = int(input("Enter a number for Fibonacci series: "))
print(Fibonacci(10))
print("Fibonacci list: ",f)
print("a =",a)
print("b =",b)