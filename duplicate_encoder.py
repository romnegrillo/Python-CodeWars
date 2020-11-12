def duplicate_encode(word):
    """
    This function takes a string input that contains any characters
    and it returns a new string containing only ")" and "(" depending
    on how many times a certain character is repeated in the string.

    The letter will be replaced by "(" if it only appears once in the string.
    Else, it should be replaced by ")".
    
    Case should be ignored.
    """
    new_string = ""
    word = word.lower()

    for letter in word:
        if(word.count(letter)>1):
            new_string += ")"
        else:
            new_string += "("

    return new_string

 
