#NOTES
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░        ⭐WHILE LOOP ⭐       ░░  => EXECUTE SOME CODE WHILE SOME CONDITION IS TRUE
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

# name = input("Please Enter Your Name: ")

# while name == "":
#     print("You did not Enter Your Name:")
#     name = input("Please Enter Your Name: ")

# print(f"Bonjour {name}")

age = int(input("Please Enter Your Age: "))

while not(1000 > age > 0):
    print("The Age you have entered is invalid")
    age = int(input("Please Enter Your Age: "))
print("You are Alive, Stay Happy")
