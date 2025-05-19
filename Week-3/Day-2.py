#NOTES

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░        ⭐ FUNCTIONS ⭐       ░░  => A BLOCK OF REUSABLE CODE, USE () TO INVOKE THE DUNCTION AFTER IT'S NAME.
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

def hbd(name, age):
    print(f"Happy Birthday To You, {name}" )
    print(f"You are now {age} Years Old.")

hbd("garry", 24)
hbd("larry", 23)


# return = statement used to end a function
#          and send a result back to the caller

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)
