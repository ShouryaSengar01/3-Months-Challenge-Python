#NOTES
# DICTIONARY = IT'S A COLLECTION OF {KEY:VALUE} PAIRS.

dict_1 = {"M.P.":"Bhopal",
          "Bihar": "Patna",
          "Jharkhand":"Ranchi",
          "Japan":"Tokyo"
          }

# print(dir(dict_1))
# print(help(dict_1))
# print(dict_1.get("Japan"))

# dict_1.update({"Germany":"Berlin"})
# dict_1.update({"M.P.": "Beijing"})
# dict_1.pop("Bihar")
# dict_1.popitem()
# dict_1.clear()
# print(dict_1)


# keys = dict_1.keys()
# for key in dict_1.keys():
#     print(key)

# values = dict_1.values()
# for value in dict_1.values():
#     print(value)

items = dict_1.items()
for key,value in dict_1.items():
    print(f"{key}:{value}")
