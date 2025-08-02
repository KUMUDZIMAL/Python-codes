#using format method
name="MY NAME IS {1} AND I AM FROM {0} I AM STUDYING {2} ENGINEERING"
naav="KUMUD"
COUNTRY="INDIA"
# print(name.format(naav,COUNTRY))
branch="cs"
print(name.format(COUNTRY,naav,branch))

#using fStrings
word="maahiye"
word2="hona"

print(f"o mere {word} jinna sona na koi hona na koi {word2}")
print(f"o mere {{word}} jinna sona na koi hona na koi {{word2}}") # to print the as it is word
print(f"{(2*80-5+7)/2}")
print(type(f"{(2*80-5+7)/2}"))

#DOCSTRINGS
def add():
    '''ADD TWO NUMBERS '''
    print("HI")
    print(add.__doc__)
add()




