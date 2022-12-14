print("")
banner = "*************** EVEN OR ODD NUMBERS ***************"
print(banner)

print("\n\nGive me a number between 1-100\n")

special_number = int(input("You number is\n"))
print("\n")

if (special_number % 2) == 0:
   print("your number {} is Even".format(special_number))
else:
   print("your number {} is Odd".format(special_number))

print("\n")
