import math

#### String ####

# literal assignment
first = "Cosmin"
last = "Boureanu"

# print("")
# print(type(first))
# print(first)
# print("")

#### Constructor Function ####

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))
# print("")

#### Concatenation ####

# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)

#### Cast a nr to str ####

# decade = str(1980)
# print(type(decade))
# print(decade)

# statemenet = "I like jazz music from the " + decade + "s."
# print(statemenet)


#### Multiple Lines ####

# multiline = """
# Salut, ce faci?

# Doar verificam.
#                     Totul bine?

# """
# print(multiline)

# # Special characters

# special = "I'm back at work!\tHey!\n\nWhere's this at\\located?"
# print(special)

# #### String Methods ####

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("bine", "ok"))
# print(multiline)

# print(len(multiline))
# multiline += "                                         "
# multiline += "                             " + multiline
# print(len(multiline))
# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

# print("")

# # Build a menu

# PROIECT MENIU CAFENEA

title = "MENU".upper()  #!!!!! Folositor !!!!!
print(title.center(20, "="))  #!!!!! Folositor !!!!!

print("")
print("Cafea cu lapte".ljust(20, ".") + "$3".rjust(4))
print("Pizza".ljust(20, ".") + "$12".rjust(5))
print("Ceai".ljust(20, ".") + "$0.98".rjust(7))
print("Croisant + Cafea".ljust(20, ".") + "$10".rjust(5))
print("Egspresso".ljust(20, ".") + "$2".rjust(4))
print("")

# string index values

print(first[1])
print(first[-1])
print(first[0:2])
print(first[1:])
print("")

# Some methods to return boolean data

print(first.startswith("C"))
print(first.endswith("B"))

# Boolean data type

value = True
x = bool(False)
print(type(x))
print(isinstance(value, bool))
print("")

# Numeric data type

# Integer type

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
print("")

# Float type

gpa = 3.27
y = float(3.14)
print(type(gpa))
print(isinstance(y, float))
print("")

# Complex type

compl_value = 5 + 2j
print(type(compl_value))
print(compl_value.real)
print(compl_value.imag)
print("")

# Build-in function for numbers

print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))
print("")

print(math.pi)
print(math.sqrt(121))
print(math.ceil(gpa))
print(math.floor(gpa))
