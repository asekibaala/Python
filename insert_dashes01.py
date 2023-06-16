def insert_dashes(a_string):
    counter = 1
    res = ""
    for cha in a_string:
        res += char
        if counter == 3:
            res += '-'
            counter = 1
        else:
            counter += 1
    return res