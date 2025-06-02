import time

timer = int(input("Please Enter the time in Seconds: "))

for _ in range(timer,0,-1):
    seconds = _ % 60
    minutes = int(_/60) % 60
    hours = int(_ / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP")


#I did this a lot before but forgot to upload so i uploaded this on day 7 coz i didn't do much on this day, went thru w3 school and revision n stuff only
