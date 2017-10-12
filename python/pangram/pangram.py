def is_pangram(sentence):
    ''' is passed a single string parameter and returns True if the input 
    contains all letters of the alphabet, or False if any letters are missing '''
    # establish sample alphabet:
    alpha_set = "abcdefghijklmnopqrstuvwxyz"
    lower_sentence = sentence.lower()
    # loop over each letter in alphabet:
    for index in range(len(alpha_set) - 1):
        current_letter = alpha_set[index]
        # look for a letter match within the input sentence
        if lower_sentence.find(current_letter) == -1:
            # return False if not found
            return False
    # if loop completes, sentence is a pangram!
    return True
