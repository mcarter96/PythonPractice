# July 20
# Given two integers, write a function to sum the numbers without using any arithmetic operators.
# Problem source: https://www.byte-by-byte.com/sum/

def sumOfTwo(a, b):
    if b == 0:
        return a
    else:
        return sumOfTwo(a^b, ((a&b) << 1))

def diffOfTwo(a, b):
    if b == 0:
        return a
    else: 
        return diffOfTwo(a^b, (~a&b) << 1)

def productOfTwo(a, b):
    if b == 0:
        return 0
    if b > 0:
       return(a + productOfTwo(a, b-1))
    if b < 0:
        return(-productOfTwo(a, -b)) 

def quotientOfTwo(a, b):
    if b == 0:
        return "Cannot divide by 0"
    
    if a < 0 ^ b < 0:
        sign = -1
    else:
        sign = 1

    dividend = abs(a)
    divisor = abs(b)

    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1
    
    return sign*quotient
    

def solveOperation():
    
    while True:
        try:
            numA = int(input("Please enter first integer: "))
        except:
            print("Please enter a valid integer")
        else:
            break
    
    while True:
        oper = input("Please enter \'+\', \'-\', \'*\', or \'/\' for operation: ")
        if oper != "+" and oper != "-" and oper != "*" and oper != "/":
            print("Please enter a valid operation")
        else:
            break
    
    while True:
        try:
            numB = int(input("Please enter second integer: "))
        except:
            print("Please enter a valid integer")
        else:
            break
    
    return numA, oper, numB

def calculate():
    a, op, b = solveOperation()
    if op == '+':
        print(str(a) + " + " + str(b) + " = " + str(sumOfTwo(a, b)))
    elif op == '-':
        print(str(a) + " - " + str(b) + " = " + str(diffOfTwo(a, b)))
    elif op == '*':
        print(str(a) + " * " + str(b) + " = " + str(productOfTwo(a, b)))
    elif op == '/':
        print(str(a) + " / " + str(b) + " = " + str(quotientOfTwo(a, b)))

def main():
    while True:
        again = input("Enter \'q\' to quit or enter to continue: ")
        if again == 'q':
            exit(0)
        else:
            calculate()

if __name__ == "__main__":
    main()