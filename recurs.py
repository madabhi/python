def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fac(n-1)

in1=int(input("Enter your number\n"))
print("Factorial is ", fac(in1))

def fun(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)

print("Fun is ", fun(in1))