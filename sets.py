'''
marks={4,3335,5,6,5}
print(marks)
'''
#score={}
'''
print(type(score))#shows type dictionary
score=set()
print(type(score))#shows type set
score={1,2,3}
marks={7,9,3}
print(score.union(marks))
#score.update(marks)
#print(score)
print(score.intersection(marks))
score.intersection_update(marks)
print(score)

marks.intersection_update(score)
print(marks)

rank={1,2,2,3,4,5,6,6}
rollno={1,5,9,10,68}
print(rank.symmetric_difference(rollno))
rank.symmetric_difference_update(rollno)
print(rank)
print(rank.difference(rollno))


rank.difference_update(rollno)
print(rank)
'''
rank={1,2,2,3,4,5,6,6}
rollno={1,5,9,10,68}
print(rank.isdisjoint(rollno))
print(rank.issuperset(rollno))
print(rank.issubset(rollno))
rank.add(96)
print(rank)
rank.remove(6)
rank.discard(4)
print(rank)
#rank.remove(100) #throws error if element to be removed is not present
#rank.discard(400) #does not throws error if element to be removed is not present
print(rank)
item=rank.pop()
print(item)
print(rank)

rank.clear()
print(rank)
del rank





