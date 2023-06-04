def char_in_string(a_string, char_to_look_for):
    for char in a_string:
        if char == char_to_look_for:
            return True
    return False