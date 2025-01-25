#Countdown Timer

import time

my_time = int(input("Enter the time in seconds: "))
#for x in range (0, my_time):
    #print(f"Time left: {my_time - x} seconds")
for x in range (my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    #print(f"00:{minutes:02}:{seconds:02}")
    #print (f"00:00:{seconds:02}")
    time.sleep(1)

print("This is a countdown timer")