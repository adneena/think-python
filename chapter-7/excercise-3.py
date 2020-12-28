import string


def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars."""
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places."""
    res = ''
    for letter in word:
        res = res + rotate_letter(letter, n)
    return res


print(rotate_word('cheer', 7))
print(rotate_word('melon', -10))
print(rotate_word('sleep', 9))