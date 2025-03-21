def check_input_type(value1, 
                     value2):
    
    value1 = float(value1)
    value2 = float(value2)

    return value1, value2

def calculator_helper(value1, value2, operation):
    if operation == 'addition':
        return value1 + value2
    elif operation == 'subtraction':
        return value1 - value2
    elif operation == 'multiplication':
        return value1 * value2
    elif operation == 'division':
        return value1 / value2
    else:
        return "Invalid operation."
    