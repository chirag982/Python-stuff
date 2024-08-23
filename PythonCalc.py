def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

answer=0
to_continue = True

#Basically using dictionary here
operations = {
              "+":add,
              "-":subtract,
              "*":multiply,
              "/":division
              }
again='n'
answer = 0
def calculator(again,answer):
    # basically this function keeps track of the previous result also and ask if we want to proceed with that result or not.
    if again=='n':
        number1 = float(input("What's the first number?"))
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation from the line above.")
        number2 = float(input("What's the second number?"))    

    elif again=='y':
        number1 = answer
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation from the line above.")
        number2 = float(input("What's the next number?"))

    else:
        print("Type only what has been asked! Please.")
        again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.").lower()
        calculator(again)
        
    calc_function = operations[operation_symbol]

    if operation_symbol=='/':
        if number2 == 0:
            print("Not valid! Proceed again.")
            calculator(again,answer)
    answer = calc_function(number1,number2)
    print(f"{number1} {operation_symbol} {number2} = {answer}")
    again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.").lower()
    calculator(again,answer)
    
calculator(again,answer)
