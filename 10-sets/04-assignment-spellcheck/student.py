def spellcheck(document, valid_words):
    document = document.lower()                  # make all words lowercase
    all_words = document.split()                 # a list of words in lowercase

    set_valid_words = set(valid_words)          # make a set out of a list of valid words
    #print(str(valid_words))

    new_words = set()
    for word in all_words:
        if not (word in set_valid_words):
            new_words.add(word)
    return new_words