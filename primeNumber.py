def primeNumber():
    n=int(input("enter a number"))
    i=2
    if n==0:
        print("0 is neither prime nor composite")
        return
    elif n==1:
        print("1 is neither prime nor composite")
        return
    elif n<0:
        print("there are no negative prime numbers")
        return
    flag=0
    while(i<=n/2):


        if(n%i==0):
            flag=1
            break

        i=i+1
    if flag==1:
        print(n,"is not a prime number")
    else:
        print(n,"is prime number")

primeNumber()