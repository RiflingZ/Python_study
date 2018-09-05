# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.


def count_words(strings):
    word = ""
    r = 0
    for char in strings:
        if char != " ":
            word += char
        else:
            if word != "":
                r += 1
            word = ""
    if not word == "":
        r += 1
    return r


passage = ("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print(count_words(passage))
# >>>56
