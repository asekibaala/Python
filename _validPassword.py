import re
password_1 = 'Jhx85a'
password_2 = 'ajd2819adkBjld'
password_3 = '81$br&j#'
password_4 = 'kp03%$Ji19Br!rdV'

## Has at least one of the following numbers: 0, 1, 2, 3

has_one_number_pwd_1 = bool(re.search(r'[0123]',password_1))
print(has_one_number_pwd_1)
has_one_number_pwd_2 = bool(re.search(r'[0123]',password_2))
print(has_one_number_pwd_2)
has_one_number_pwd_3 = bool(re.search(r'[0123]',password_3))
print(has_one_number_pwd_3)
has_one_number_pwd_4 = bool(re.search(r'[0123]',password_4))
print(has_one_number_pwd_4)

## Has at least one of these characters, v, V, r, R, b, B.
at_least_one_symbol_pwd_1 = bool(re.search(r'[vVrRbB]', password_1))
at_least_one_symbol_pwd_2 = bool(re.search(r'[vVrRbB]', password_2))
at_least_one_symbol_pwd_3 = bool(re.search(r'[vVrRbB]', password_3))
at_least_one_symbol_pwd_4 = bool(re.search(r'[vVrRbB]', password_4))

## Has at least one symbol: $%#&
at_least_one_symbol_pwd_1 = bool(re.search(r'[$%#&]', password_1))
at_least_one_symbol_pwd_2 = bool(re.search(r'[$%#&]', password_2))
at_least_one_symbol_pwd_3 = bool(re.search(r'[$%#&]', password_3))
at_least_one_symbol_pwd_4 = bool(re.search(r'[$%#&]', password_4))


"""
This code uses the  re  module to search for a regular expression 
pattern in each password string. Specifically, it searches for 
the pattern  [0123] , which matches any single character that is
 either 0, 1, 2, or 3. The  re.search()  function returns a match 
 object if the pattern is found in the string, or  None  if it is 
 not found. We then convert the match object to a boolean value 
 using the  bool()  function, which returns  True  if the match object is not  
 None , and  False  otherwise.
"""