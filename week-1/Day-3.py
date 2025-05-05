# Watched the python video till 1 hour and completed the calculator project today. 
#Here are the Notes

name = input("Please Enter Your Name: ")
if name == "":
    print("Enter yourrr name!!")
    name = input("TYPE ITT HERE:")
      
    if name == "":
        print("Wanna Continue it or not ?? (Y/N)")
        answer = input("->")        
        if answer == "Y":
            name = input("Enter The Name: ")
        else:
            print("See ya later")

if name != "":
    print(f"Hello {name}")


# name = input("Please Enter Your Name: ")

# if name == "":
#     print("Enter your duckin name!!")
#     name2 = input("TYPE ITT HERE: ")

#     if name2 == "":
#         print("See ya later...")
#     else:
#         print(f"Cool, Welcome {name2}")
# else:
#     print(f"Hello {name}")
#     exit()
