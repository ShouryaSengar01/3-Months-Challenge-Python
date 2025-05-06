#Learned about mathmematic operators and made a small Fizbuzz prject kinda thing using the if and else statements i learned yesterday.


#NOTES
friends = 10

# friends +=1
# friends -= 2
# friends *= 4
# friends /= 5
# friends %= 6
# friends **= 2

print(friends)


#FIZBUZZ
for _ in range(1, 101):
    if _ % 3 == 0 and _ % 5 == 0:
        print("FIzzBuzz")
    elif _ % 3 == 0:
        print("Fizz")
    elif _ % 5 ==0:
        print("Buzz")
    else:
        print(_)  
