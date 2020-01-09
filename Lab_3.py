import sys

def conditionals(n) :
    
    if (n % 2 > 0 and n > 60) :
        return "Odd and over 60."
    elif (n % 2 == 0 and n >= 2 and n < 25) :
        return "Even and less than 25."
    elif (n % 2 == 0 and n >= 26 and n <= 60) :
        return "Even."
    elif (n % 2 == 0 and n > 60) :
        return str(n) + ": Even."
    elif (n % 2 > 0):
        return str(n) + ": Odd."
        

def main(n):
    cont = "y"
    while (cont == "y") :
        response = input("Please enter a number between 1 and 100: ")
        response = int(response)
        while (response < 1 or response > 100) :
            response = input("Invalid input. Please enter a number between 1 and 100: ")
            response = int(response)
        result = conditionals(response)
        print(result)
        cont = input("continue? (y/n): ")
    

if __name__ == '__main__':
    sys.exit(main(sys.argv))
