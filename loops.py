

COLORS=["red","pink","orange"]
for color in COLORS:
    print(color)
    for i in color:
        print(i)

for i in range(1,10,3):
    print(i)


i=0
while(i<=30):

    i=int(input("ENTER VALUE OF i"))
    print(i);
    i=i+1;

else:
    print("done with loop")


for i in range(6):
    if i==1: continue
    print(i)
    if i==4:
        break


else:
    print("done with loop")


#do-while loop emulation in python
i=0
while True:
    print(i)
    i=i+1
    if i==4:
        print(i+100)
        break


