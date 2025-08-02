'''
try:
    print(jgg)
except Exception as e:
    print(e)

try:
    n=int(input("enter a number"))
except ValueError:
    print("its not a number")
print("out of")
try:
  num=int(input("enter a number"))
  a=[9,8]
  print(a[num])
except IndexError:
    print("invalid index")
print("out of")

try:
    print(jgg)
except:
    print("wrong")
finally:
    print("i am always executed")
    '''

def func1():
    try:

        print(jgg)
        return 1
    except:
        print("wrong")
        return 0
    finally:
        print("i am always executed")
    #print("i am always executed")
func1()

