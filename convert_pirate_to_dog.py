def convert_pirate_to_dog(pirate_saying):
    result_in_dog_speak = "" """we create a new string because strings are immuatable"""
    for letter in pirate_saying:
        result_in_dog_speak += letter
        result_in_dog_speak += "oo"
    return result_in_dog_speak