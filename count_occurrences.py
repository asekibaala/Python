def count_occurrences(a_list):
    result_dict = {}
    for elem in a_list:
        if elem not in result_dict.keys():
            result_dict[elem] = 1
        else:
            result_dict[elem] += 1
    return result_dict

"""
function that receives a list as input and returns a dictionary 
that counts how many times the data in the list is repeated.

count_occurrences(["a", "b", "c", "a", "a", "b"])

# {"a" : 3, "b" : 2, "c": 1}

"""