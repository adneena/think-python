'''
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
'''


def is_anagrams(first_word, second_word):
    if sorted(first_word) == sorted(second_word):
        return True
    else:
        return False


print(is_anagrams('silent', 'vilont'))
print(is_anagrams('silent', 'listen'))
