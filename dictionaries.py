dict1={123:"priya",124:"harshita",125:"tara",126:"sara",127:"megha"}
dict2={128:"naira",129:"shanaya",130:"natasha"}
print(dict1)
print(dict1[125])
print(dict1.keys())
print(dict1.values())
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)

print(dict1.items())
print(dict1.get(1)) #doesnt throw error if key is not present in the dictionary
#print(dict[1]) #throws error if key is not present in the dictionary
dict1.update(dict2)
print(dict1)
del dict1[128]
print(dict1)
dict1.clear()
print(dict1)
del dict1
#print(dict1)
dict2.popitem()
print(dict2)
dict2.pop(129)
print(dict2)

