def is_isogram(string):
    ''' takes a single string as an input parameter and returns True if all alpha 
    characters in the string are unique, and False if there are any duplicate letters '''
    lower_string = string.lower()
    # examine each letter in string
    for index in range(len(lower_string) - 1):
        current_letter = lower_string[index]
        if current_letter.isalpha():
            # compare letter with all other letters
            match_check = lower_string.find(current_letter, index + 1)
            # if letter matches another letter: return false
            if match_check != -1:
                return False
    # if all alpha chars are unique:
    return True

