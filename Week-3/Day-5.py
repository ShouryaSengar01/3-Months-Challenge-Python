# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░       ⭐ ITERABLES ⭐      ░░  => An Object/Colellction that can return its elements one at a time, 
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     allowing it to be iterated over in a loop.

numbers = [1, 2, 3 ,4 ,5 ] #list iteration
for num in reversed(numbers): 
    print(num)

fruits = {"apple", "pineapple", "litchi", "strawberry"}  #set iteration
for _ in fruits: 
    print(_)

name = "Ben Tennyson" #string iteration
for x in name:
    print(x, end= "#")

my_dict = {"A":1, "B":2, "C":3, "D":4} #dictionary iteration

for key, value in my_dict.items():
    print(f"{key}:{value}")
