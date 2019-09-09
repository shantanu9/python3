# function

def add(x,y):
    return (x+y)

a = 1
b = 3

print (add(a,b))


def fibo(n):
    a = 0
    b = 1
    for x in range(n):
        a=b
        b=a+b
        print (a,'\n')
    return b
num = int((input("enter the value of n:"))
fibo(num))
