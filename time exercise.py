import time
if int(time.strftime('%H'))<12 and int(time.strftime('%H'))>=4:
    print("GOOD MORNING");
elif int(time.strftime('%H'))>=12 and int(time.strftime('%H'))<16:
    print("GOOD AFTERNOON");
elif int(time.strftime('%H'))>=16 and int(time.strftime('%H'))<22:
    print("GOOD EVENING");
else:
    print("GOOD NIGHT");

'''
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
print(timestamp)
timestamp=int(time.strftime('%M'))
print(timestamp)
timestamp=int(time.strftime('%S'))
print(timestamp)
'''