import random

print("welcome to ultimate jackpot")
#print(input("press any key to begin..."))

a = random.randrange(1, 5)
b = str(input("input guess: "))

print("answer = " + str(a))
#print("your answer = " + str(b))

if str(a) == str(b):
    print("correct, u win")
else:
    print("wrong, u lose")
