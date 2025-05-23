#NOTES
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░      ⭐ KEYWORD ARGUMENTS ⭐      ░░  => An Argument preceded by an identifier, Helps with readabilty
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     Orders of Arguments doesn't matter
#                                              Types=> 1. Positional  2.Default 3.Keyword 4. Arbitary

# def hello(greeting, title, first, last):
#     print(f"{greeting.title()}, {title.title()} {first.title()} {last.title()}")

# hello("hello", last="Tennsyon", first="Ben", title="Cool")

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░      ⭐ ARBITARY ARGUMENTS ⭐      ░░  => *args = allows you to pass mutlpile non-key arguments
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      **kwargs = allows you to pass mutliple keyword arguments
#                                              (* is the unpacking operator, u can use anyword after it like *num or **num)


#📖📖ARGS📖📖
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(2,5,3,0))

# def display_name(*args):
#     for name in args:
#         print(name, end=" ")

# display_name = ("Scientist","Spongebob", "Squarepants", )


#--------------------------------------------------------------------
#📖📖KWARGS📖📖

# def print_add(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_add(street = "Maple St.",
#           house_number = "28",
#           city = "gerogia",
#           state = "d.c.",
#           zip = "15275")

#---------------------------------------------------------------------
#EXERCISE

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end="")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')}{kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob ", "Squarepants ",
               street = "Maple Street",
               pobox = "PO box #69",
               city = "Jacksonville",
               state = "Florida",
               zip = "32034")
