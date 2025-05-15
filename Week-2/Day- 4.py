#NOTES
#Format Specifier = {value:flags} format a value based on what flags are inserted.

# ▂▃▄▅▆▇█▓▒░  KeyPoints  ░▒▓█▇▆▅▄▃▂

# .(number)f = round to that many decimal places (fixed point)
# :(number)  = allocate to many places
# :03  = allocate and zero pad that many places
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive plus
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3000.141
price2 = -987.65
price3 = 12051.34

print(f"Price 1 is {price1:.2f}")   #Digits you want after a Decimal
print(f"Price 2 is {price2:.1f}")
print(f"Price 3 is {price3:.0f}")

print("-----------------------------------------")

print(f"Price 1 is {price1:5}")   #Allocate the number of spcaes before the value, It's gotta be more than the value itself so if the value consists of 5 digit u will have tu input 6 to add a space of 1
print(f"Price 2 is {price2:15}")
print(f"Price 3 is {price3:10}")

print("-----------------------------------------")

print(f"Price 1 is {price1:05}")   #Allocate the number of spcaes and adds zero on that place before the value, "Same as above"
print(f"Price 2 is {price2:015}")
print(f"Price 3 is {price3:010}")

print("-----------------------------------------")

print(f"Price 1 is {price1:<5}")   #Left allignment
print(f"Price 2 is {price2:>15}")  #Right allignment
print(f"Price 3 is {price3:^10}")  #Centre allignment

print("-----------------------------------------")

print(f"Price 1 is {price1:+}")   #Preseeds any positive value with "+" sign
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3: }")   #You can just leave a space to allign them too

print("-----------------------------------------")

print(f"Price 1 is {price1:,}")   #Separates by thousands with comma
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3:,}")

print("-----------------------------------------")

print(f"Price 1 is {price1:+,.2f}")   #Mixing the operators
print(f"Price 2 is {price2:+,.2f}")
print(f"Price 3 is {price3:+,.2f}")

