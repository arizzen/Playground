print("1.Addition = +")
print("2.Subtraction = -")
print("3.Multiplication = *")
print("4.Division = /")
a = float(input("input 1st digit: "))
b = float(input("input 2nd digit: "))
c = (input("please select an operator from the above menu: "))
if c == '1':
    d = a + b
    print(d)
if c == '2':
    d = a - b
    print(d)
if c == '3':
    d = a * b
    print(d)
if c == '4':
    d = a / b
    print(d)