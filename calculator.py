
basicoperators = ["+", "*", "/", "-"]
print("here is the list of operators available to use: ", basicoperators)

firstnumber = input("first number: ")
operator = input("operator: ")
secondnumber = input("second number: ")


if operator in basicoperators:
    if operator == "+":
        answer = int(firstnumber) + int(secondnumber)
        print(firstnumber, " + ", secondnumber, " = ", answer)
    elif operator == "*":
        answer = int(firstnumber) * int(secondnumber)
        print(firstnumber, " * ", secondnumber, " = ", answer)
    elif operator == "/":
        answer = int(firstnumber) / int(secondnumber)
        print(firstnumber, " / ", secondnumber, " = ", answer)
    elif operator == "-":
        answer = int(firstnumber) - int(secondnumber)
        print(firstnumber, " - ", secondnumber, " = ", answer)



