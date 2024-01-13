def fill_matching_letters_in_blank_spaces(actual_word, guess_word, letter):
    # Converting string to list such that character at any specific position can be modified.
    guess_word = list(guess_word)

    # Checks one by one that the correctly guessed letter occurs at which numbered place in the original word.
    i = 0
    replacements = 0
    while i < len(actual_word):
        # Matching index found at which correctly guessed letter occurs.
        if letter == actual_word[i] and guess_word[i*2] == "_":
            # For each letter in original word, guess word contains two chars: '_ ', thus modification 
            # must only replace the underscore '_', which occurs at every even index.
            guess_word[i*2] = letter
            replacements += 1
        i += 1

    # After all modifications, joining all the characters in the list to retrieve the string.
    guess_word = "".join(guess_word)
    return (guess_word, replacements)



def hint(actual_word, guess_word):
    # This function will add one letter to the blank space, only if there is more than 1 blank.
    if guess_word.count("_") > 1:
        # Converting string to list such that character at any specific position can be modified.
        guess_word = list(guess_word)
        for i in range(0, len(guess_word), 2):
            if guess_word[i] == "_":
                guess_word[i] = actual_word[i//2]
                break

        # After all modifications, joining all the characters in the list to retrieve the string.
        guess_word = "".join(guess_word)
    return guess_word