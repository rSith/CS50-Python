expression = input("Expression: ")
x, y, z = expression.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    if int(z) != 0:
        print(float(x) / float(z))
    else:
        print("undefined")
else:
    print("invalid operator")