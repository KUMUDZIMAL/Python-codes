def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

c=factorial(6)
print(c)

def fibonacci(n):
    a=0
    while(n!=0):
        a=fibonacci(n-1)+fibonacci(n-2)
        n=n-1
    print(a)
fibonacci(10)