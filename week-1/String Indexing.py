#This is a small String Indexing project kinda thing I made
#INDEXING - accessing elements of a sequence using [] i.e. indexing operator
#           [start:end:step]
# 🌟 KEY POINTS 🌟
# 1️⃣ Indexing Starts from 0 in positive and -1 in negative.
# 2️⃣ While indexing or splitting a string, the input u give in "end" place doesn't get included.
# 3️⃣ When an colon is left empty, python consider it as default i.e. from start or till end.

credit_number = "6534-4538-9481-0026"

# print(credit_number[0])    🔲Prints the value on first place.
# print(credit_number[:4])   🔲Prints from first place to the 4th. 
# print(credit_number[5:9])  🔲Prints the second set of digits.
# print(credit_number[5:])   🔲Prints from 5th place to the end.
# print(credit_number[-1])   🔲Prints the last, example of negative indexing.
# print(credit_number[::2])  🔲Prints Every second character, basically skips one and print the one after it.
# print(credit_number[::-1]) 🔲Reverses the whole string.

# ▂▃▄▅▆▇█▓▒░  EXERCISE  ░▒▓█▇▆▅▄▃▂
#Print the last 4 digit of cc no. to keep it encrypted

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
