def insert_dashes(string):
    return '-'.join([string[i:i+3] for i in range(0, len(string), 3)])


"""
This function uses Python's string slicing and  join  methods to insert dashes every 3 characters. 
The list comprehension  [string[i:i+3] for i in range(0, len(string), 3)]  
creates a list of substrings of  string  that are 3 characters long. 
The  join  method then joins these substrings together with dashes to create the final string.

"""