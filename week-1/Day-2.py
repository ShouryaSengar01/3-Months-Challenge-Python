#Today I completed the video I was doing yesterday till 52 hour timestamp and completed the MADLIBS project alongside it. Learned statements and some more about numbers.
# HERE ARE MY NOTES FOR TODAY
#  ______                           __  _          
# /_  __/_ _____  ___ _______ ____ / /_(_)__  ___ _
#  / / / // / _ \/ -_) __/ _ `(_-</ __/ / _ \/ _ `/
# /_/  \_, / .__/\__/\__/\_,_/___/\__/_/_//_/\_, / 
#     /___/_/                               /___/  

# ╔════════════════════╗
# ║  WITH TYPECASTING  ║
# ╚════════════════════╝
'''
name  = input("Please enter your name")
is_name = bool(name)
if is_name == True:
    print("Hello", name)
else:
    print("Kindly enter your name")
'''
# ╔════════════════════════════════╗
# ║  TYPECASTING (MORE PYTHONIC)   ║
# ╚════════════════════════════════╝
'''
name = input("Please enter your name: ")
is_valid = bool(name)  # Store the boolean value in a separate variable

if is_valid:
    print("Hello", name)  # Use the original name variable
else:
    print("Kindly enter your name")
'''
# ╔═══════════════════════════════════════╗
# ║  WITHOUT TYPECASTING(MOST PYTHONIC)   ║
# ╚═══════════════════════════════════════╝
'''
name = input("Please enter your name: ")
if name:  # This checks if name is not empty
    print("Hello", name)
else:
    print("Kindly enter your name")
'''
#AND HERE IS THE PROJECT I DID TODAY

#Madlibs is a game where you create story with words

place = input("Enter the place: ")
verb = input("Enter a verb without gerund: ")
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
noun2 = input("Enter another noun: ")
color = input("Enter a color: ")
animal = input("Enter an animal: ")
verb2 = input("Enter another verb with gerund: ")


print(f"One day, I decided to go to a {place} to {verb}.")
print(f"I packed my {noun} and my {adjective} {noun2}.")
print(f"When I arrived, I saw a {color} {animal} {verb2}")
print(f"and a {adjective} human {verb2} with my {noun}")
