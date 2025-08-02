import random
def secret_code():
    string=input("enter any string")
    fl=string[0]
    print(string)
    if len(string)==1:
        print("secret code:",string)
    elif len(string)==2:
        reversed_string=string[::-1]
        print("secret code:",reversed_string)
    else:
       print(string)
       string=string[1:]
       character=["hgf","hjr","eyi","yue","egu","git","ghh","rty","fdh","dfj","rgf","jeg","uht","kgt","fkt","for","kjd","vfh","fie","irw","euf","eue","ili","eee","kuh","ruk","kgr","fej","ank"]
       random_chars1=random.choice(character)
       random_chars2=random.choice(character)
       print("secret code:",random_chars1+string+fl+random_chars2)
secret_code()