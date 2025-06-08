

def perform_operation(x , y , action):
    if action == "add":
        return x + y
    elif action == "subtract":
        return x - y
    elif action == "multiply":
        return x * y
    elif action == "divide":
        if y == 0:
            print("yasd")
            return None
        else:
            return x / y
    else:
        return None
    
