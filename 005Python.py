my_name = "Abel Sekibaala"

print(len(my_name))
print(my_name)
print(my_name[7])
print(my_name[4:9])
print(my_name[-6])

subject = "welcom {}!"
print(subject.format(my_name))

today = "Today is {}, {}, {}"
msg = today.format("Sunday", "June", 4)

print(msg)