# strings are immutable
'''
NAME="KUMUD ZIMAL!!!"
print(len(NAME));
print(NAME.upper()); #it returns new string
print(NAME.lower());  #it returns new string
print(NAME); #original string remains same as strings are immutable
print(NAME.rstrip("!!!LAM"));
print(NAME.replace("KUMUD","SANGITA"));
print(NAME.split(" "));
TEXT="hii to everyone"
print(TEXT.capitalize());
print(TEXT.title());
str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
print(NAME.count("Harry"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())
str1 = "WelcometotheConsole000!!!"
print(str1.endswith("!!!"))
print(str1.endswith("to",7,10))
print(str1.startswith("Wel"))
print(str1.find("the"))
print(str1.index("the"))
'''
'''
str1 = "WelcometotheConsole99!!!"
print(str1.isalnum())  # I  have doubt in this
str1 = "Welcome"
print(str1.isalpha())
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
str1 = "We wish you a Merry Christmas\n"
print(str1.istitle())
'''
str1="kumud   "
print(str1.isspace())  #it will return false
str1="    "
print(str1.isspace()) #it will return true
