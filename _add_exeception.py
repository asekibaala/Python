def add(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return None
    return x + y

"""
This implementation uses the  isinstance()  function to check if both  x  
and  y  are either integers or floats. If either of them is not a number, 
it returns  None . If both of them are numbers, it performs the addition 
and returns the result. With this implementation, the test you provided 
should pass without raising an exception.
"""