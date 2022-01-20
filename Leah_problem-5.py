def fermat():
    # condition for the equation
    num1 = abs(int(input("enter num1:")))
    num2 = abs(int(input("enter num2:")))
    num3 = abs(int(input("enter num3:")))
    n: int = abs(int(input("enter n:")))
    eqn = num1**n + num2**n
    c = num3**n
    # condition for the equation

    if eqn != c:
        print("Did not satisfy!")
        return f"Fermat near misses has been proven where power of num1 to {n} and power of num2 to{n}  is: {eqn} and is not equal to {c}"
    else:
        return f"There exists a solution where num1 is {num1},  num2 is {num2} and solution is {c}"


x=fermat()
print(x)