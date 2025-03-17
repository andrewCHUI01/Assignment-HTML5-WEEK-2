number1= 10
number2 = 12.7
print(number2)


print("Hello world!")
# Datatypes


myname = "Andrew Musau"
print(myname)





languages = [1,2,3,4,5,6,7]
print(languages)
print(languages[3])





def calculator():
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+ or -): ")
        
        # Perform the calculation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        else:
            print("Invalid operation. Please enter + or -.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
