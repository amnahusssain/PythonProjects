import time

timestamp = time.strftime('%H:%M:%S')

hour = int(time.strftime('%H'))
minute=int(time.strftime('%M'))
second=int(time.strftime('%S'))

print("The time right now is ",timestamp)

if  (6<= hour <=11):
    print("Good Morning")
elif (18<= hour <=23):
    print("Good Evening")
elif(12<= hour <=17):
    print("Good Afternoon")
else:
    print("Good Night")



