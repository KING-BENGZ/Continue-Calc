print("Hello bros. Let's start with a calculator")

def Calculator():
    print("Pick a number")
    numberOne = int(input())
    print("Pick another number")
    numberTwo = int(input())
    print("Press 1 to add and 2 to subtract")
    selected = int(input())
    
    if selected == 1:
        x = numberOne + numberTwo
        print(numberOne, "plus", numberTwo, "is", x)
    elif selected == 2:
        y = numberOne - numberTwo
        print(numberOne, "minus", numberTwo, "is", y)
    else:
        print("You didn't pick either 1 or 2")
        return False 
    
    return True  

# First call to the Calculator function
while Calculator():
    pass  # The loop will continue as long as Calculator() returns True
