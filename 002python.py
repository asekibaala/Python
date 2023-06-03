x = 3 + 2 #binary operator

print(x)

print(7 - 3) 

print(5/2)

y = (5).__add__(3)

print(y)

y *=2

print(y)

print('a'=='b')
print(4>2)
print(2==2)
print(2>=1)

print('e' in "Hello world")
print('x' in "Hello world")

password = "abc%"
has_special_char = '$' in password

print(has_special_char)

x = None
print(x is None)

active = True
print(active is True)

closed = False
print(closed is False)

user_is_active = False


if not user_is_active:
    print("You cant perform this task")
else:
    print("All good.processing your request")