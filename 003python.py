def operate(operation,x,y):
    if operation == 'sum':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        return x / y
    
print("==== Sum ====")
print(operate('sum',2,3,))

print("==== Subtract ====")
print(operate('subtract',2,5))
print(operate('subtract',5,2))

print("==== Multiply ====")
print(operate('multiply',2,3))

def my_function(x):
    return x * 2

print(my_function(265))