#NOTES
# Collection = single "variable" used to store multiplr values.
#   List []  = Ordered and mutable, Duplicate "OK". 
#   Tuple () = Unordered and immutable, but Add/Remove "OK". "NO" Duplicates
#   Set {}   = Ordered and Immutable. Duplicates "OK". Faster

fruits = ("Apples", "Oranges", "Pomegranate", "Coconut", "Coconut")

# print(fruits[:2])
# print(dir(fruits))
# print(help(fruits))
# print("Pineapple" in fruits)
# for fruit in fruits:
#     print(fruit)

# ▂▃▄▅▆▇█▓▒░  LIST EXAMPLES  ░▒▓█▇▆▅▄▃▂

#🔲 fruits[0] = "\"Pineapple\""
#🔲 fruits.append("Papaya")
#🔲 fuits.remove("apple")
#🔲 fruits.insert(1, "Guava")
#🔲 fruits.pop()
#print(fruits)

# ▂▃▄▅▆▇█▓▒░  TUPLE EXAMPLES  ░▒▓█▇▆▅▄▃▂

print(fruits.index("Coconut"))
print(fruits.count("Coconut"))

# ▂▃▄▅▆▇█▓▒░  SET EXAMPLES  ░▒▓█▇▆▅▄▃▂

#🔲 fruits.add("Pineapple")
#🔲 fruits.remove("Pomegranate")
# print(fruits)

