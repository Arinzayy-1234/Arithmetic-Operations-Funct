


def safe_divide(numerator, denominator):
    
    try:
        num_float = float(numerator)
        denum_float = float(denominator)
        return f'The result of the division is {num_float/denum_float}'
        
    
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero.'
    
    except ValueError:
        return 'Error: Please enter numeric values only.'
    
    
        
        

