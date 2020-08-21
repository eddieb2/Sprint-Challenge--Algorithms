'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # track the number of 'th' occurrences
    # track length of word
    word_length = len(word)

    # base case -> once we slice the word far enough it will have a length of 0 and will stop recursion
    if word_length == 0:
        return 0
    # returns our count + calling the fn again with the shortened word 1 letter over
    elif word[:2] == 'th':
        return 1 + count_th(word[1:])
    # calling the fn again with the shortened word 1 letter over
    else:
        return count_th(word[1:])
