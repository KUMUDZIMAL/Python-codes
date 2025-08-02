x=int((input("enter value of x ")))
match x:
 case 1: print(" wrong value of x")
 case 10: print(x);
 case _ if x!=25:print("x is not equal to 25")
 case _ if x!=35:print("x is not equal to 35")
 case _:print("default")