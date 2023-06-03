#flow control Guess a nummber

answer =  9 #hardcorded answer

users_guess = input('Guess a number:')

guess_as_int = int(users_guess)

if guess_as_int == answer:
    print("You guessed correctly!")
else:
    print("Incorrect guess :|")

counter = 0
 
while counter < 4:
    print("Yet to be a SE in a Cyber Security Engineer")
    counter += 1


counter = 1

while counter <= 4:
    print("Number {}".format(counter))
    counter += 1


def calculate(op,x,y):
    def add():
        return x + y
    def subtract():
        return x - y
    def multiply():
        return x * y
    def divide():
        return x / y
    
    if op == 'add':
        return add()
    if op == 'subtract':
        return subtract()
    if op == 'multiply':
        return multiply()
    if op == 'divide':
        return divide()
    
print(calculate('add',2,7))
    
