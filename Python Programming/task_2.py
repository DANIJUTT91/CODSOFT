
while 1:
    print("Simple Calculator")

    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
    except:
        print('Invalid input')
        continue
        
    print("Operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nEnter e for exit")
    choice = input("Enter operation (1/2/3/4): ")
    
    if choice == 'e' or choice == 'E':
        print('----Exit----')
        break
    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        if num2 == 0:
            print('Can\'t devide by zero.')
            continue
        result = num1 / num2
    else:
        print("Invalid operation choice")
        continue
   
    print("Result:", result)
