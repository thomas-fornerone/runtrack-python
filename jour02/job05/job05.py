def calcule(num1, operator, num2):
    return eval(str(num1) + operator + str(num2))

print(calcule(18, "+", 34))
print(calcule(34, "-", 18))
print(calcule(5, "*", 4))
print(calcule(50, "/", 2))
print(calcule(10, "%", 3))
