tup=(1)
print(type(tup)) #this shows type int
tup=(1,)
print(type(tup)) # this shows type tuple
#to find reason about above behaviour watch video no 24
countries=("india","finland","UAE","USA","UK","FRANCE")
temp=list(countries)
temp.pop();
temp.insert(2,"THAILAND");
temp[1]="italy"
print(temp)
countries=tuple(temp)
print(countries)
c=countries.index("india")
print(c)
c=countries.count("india")
print(c)
continents=("ASIA","AFRICA","EUROPE","AUSTRALIA","SOUTH AMERICA","NORTH AMERICA")
world=countries+continents
print(world)
name="shjdulk"
print(name.find("u"))
