import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@$*!(){}[]-_+\|."

all = lower + upper + numbers +symbols
length = 16
password = "".join(random.sample (all,length))
print("Here is your 16 digit Password")

print(password)

print("Enjoy!")
print("Please note that this is completely random and it is nearly impossible to generate the same exact password")
print("if there is a Character that you cannot use for your password simply just remove the character and you should be fine")
