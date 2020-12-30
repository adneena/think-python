'''
Two words are “rotate pairs” if you can rotate one of them and get the other 
Write a program that reads a wordlist and finds all the rotate pairs. Solution: http: //
thinkpython. com/ code/ rotate_ pairs. py .
'''

from rotate import rotate_word


def make_word_dict():
    """Read the words in words.txt and return a dictionary
    that contains the words as keys"""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def rotate_pairs(word, word_dict):
    """Prints all words that can be generated by rotating word.
    word: string
    word_dict: dictionary with words as keys
    """
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)


word_dict = make_word_dict()

for word in word_dict:
    rotate_pairs(word, word_dict)