'''
import math
import random
print(random.choice(questions))
'''

print("Note:Type 'quit' in place of answer if you wish to quit the game")
questions=[["WHAT IS THE CAPITAL OF MEGHALAYA","shillong","dispur","aizwal","kolkata"],
["WHAT is rusting","hg","jk","jg","gyg"],
["what is tinning","khk","klj","fg","htu"],
["what is ionization","yku","gy","hu","jaan"],
["what is information technology","paani","jabse","anjaani","ambarsiya"],
["WHAT IS THE CAPITAL OF ASSAM ","shillong","dispur","aizwal","kolkata"]]
levels=["NICE START","YOU WON 10,000 RS","NICEEE","YOU WON 15OOO RS","EXCELLENT","YOU WON 30,000RS "]
ans1=questions[0][1]
ans2=questions[1][2]
ans3=questions[2][2]
ans4=questions[3][3]
ans5=questions[4][4]
ans6=questions[5][2]
ANSWER=[ans1,ans2,ans3,ans4,ans5,ans6]
# 1 ans answered correctly 0Rs
# 2 ans answered correctly 10,000Rs
# 3 ans answered correctly 10,000Rs
# 4 ans answered correctly 15,000Rs
# 5 ans answered correctly 15,000Rs
# 6 ans answered correctly 30,000Rs
#print(ANSWER)
quit_case=["sorry! you can't take anything to home","sorry! you can't take anything to home","congrats! you won 10,000Rs ","congrats! you won 12,000Rs ","congrats! you won 15,000Rs","congrats! you won 17,000Rs"]


j=1
l=0
r=0
for i in questions:

    k=1

    print(i[0])




    for j in i[1:5]:

        print(k,".",j)


        k=k+1
    ans=input("enter ans\n")
    if ans==ANSWER[l]:
        print("RIGHT!")

        print(f"{levels[l]}")
    elif ans=="quit":
        print(quit_case[r])
        break

    else:
        print(f"sorry correct ans is {ANSWER[l]}!you lost the game")
        break

    if l==len(ANSWER)-1:
        print("CONGRATULATIONS!,YOU WON THE GAME")

    l=l+1
    r=r+1

