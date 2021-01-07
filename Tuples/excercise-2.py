from collections import defaultdict

with open(r'C:\Users\Aradh\Documents\wow.txt', 'r') as fd:
    words = fd.read().splitlines()


def make_anagram_dict(word_list):
    """Take a list of words, return a dict with a fingerprint as the key
    and the anagrams made from that fingerprint as the value."""
    result = defaultdict(list)
    for word in word_list:
        fp = ''.join(sorted(word))
        result[fp].append(word)

    result = {fp: result[fp] for fp in result if len(result[fp]) > 1}
    return result


anagrams = make_anagram_dict(words)


def print_anagrams(anagrams):
    """Uses a generator to call and print 5 items from mydict"""
    fp = (fp for fp in anagrams)

    print("Sample from anagram dict:")
    for i in range(1, 6):
        # call once, print twice
        fp_next = fp.next()
        print("%s) %s:" % (i, fp_next), anagrams[fp_next])

    print("...")
    print("\n")


print_anagrams(anagrams)


def sort_anagrams(anagrams):
    """Returns a list of lists containing all anagram matches. The longest list
     (most anagrams) is at the top"""
    anagrams_lists = []
    for fp in anagrams:
        anagrams_lists.append(anagrams[fp])
    anagrams_lists.sort(key=len, reverse=True)

    print("Most anagrams:")
    for i in range(0, 5):
        print("%s) %d" % ((i + 1), len(anagrams_lists[i])), anagrams_lists[i])
    print("...")
    print("\n")


sort_anagrams(anagrams)


def find_bingos(anagrams):
    """Filters mydict for keys of length 8. Sorts a list of the values
     (lists) and sorts by length in reverse order"""
    candidates = [anagrams[key] for key in anagrams if len(key) == 8]
    candidates.sort(key=len, reverse=True)

    print("Top Bingos:")
    for i in range(0, 5):
        fp = ''.join(sorted(candidates[i][0]))
        print("%s) %d: %s" % ((i + 1), len(candidates[i]), fp), candidates[i])

    print("...")
    print("\n")


find_bingos(anagrams)


def is_metathesis(reference, test):
    """If two anagrams mismatch exactly twice they are metathesis pairs.
     Caution: This function assumes strings of equal length"""
    i = 0
    count = 0
    while i <= (len(reference) - 1):
        if reference[i] != test[i]:
            count += 1
        i += 1
    if count == 2:
        return True
    return False


def find_metathesis(anagrams):
    """mydict values are lists, we use index 0 as a reference and check the
     rest of the list (1 to end of list) against that reference word."""
    answer = []
    for fp in anagrams:
        reference = anagrams[fp][0]
        for i in range(1, (len(anagrams[fp]) - 1)):
            test = anagrams[fp][i]
            if is_metathesis(reference, test):
                answer.append([reference, test])

    print("Sample of metathesis pairs:")
    for i in range(0, 5):
        print("%s)" % (i + 1), answer[i])
    print("...")


find_metathesis(anagrams)