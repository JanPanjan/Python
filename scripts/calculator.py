def get_number_input():
    """funkcija dobi dve številki od userja.
    Vrne polje velikosti 2."""
    num1 = input("Vnesi prvo število: ")
    num2 = input("Vnesi drugo število: ")
    nums = [int(num1), int(num2)]
    return nums

def get_operation_input():
    """Dobi input operacije. + ali - ali * ali /."""
    valid_znaki = ['+', '-', '*', '/']
    ok = True
    while ok:
        operation = input("Vnesi operacijo (+, -, *, /): ")
        for i in range(0, len(valid_znaki)):
            if operation == valid_znaki[i]:
                return operation
        print("Napačen vnos.")

def calculator():
    """Izračuna nekaj z dvemi števili."""
    nums = get_number_input()
    num1 = nums[0]
    num2 = nums[1]
    operation = get_operation_input()

    print("Rezultat: ", end='')
    if operation == '+':
        print(num1 + num2)
        return 
    elif operation == '-':
        print(num1 - num2)
        return 
    elif operation == '*':
        print(num1 * num2)
        return 
    elif operation == '/':
        print(num1 / num2)
        return 
    else:
        print("error in operation input.")
        return

calculator()

