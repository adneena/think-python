'''
Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?
'''
import time


def methodtest1(listone):
    print("here comes the first run")
    f = open('./words.txt', 'r')

    a = time.time()
    listone = []
    for i in range(113809):
        word = f.readline()
        listone = listone+[word]
    b = time.time()
    print(b-a0
    f.close()
    print("not bad")
    print("\n")
    
    
def methodtest2(listtwo):
    print("here comes the 2nd run")
    fb = open('./words.txt', 'r')
    a = time.time()
    for i in range(113809):
        word = fb.readline()
        listtwo.append(word[:-2])
    b = time.time()
    print(b-a)
    fb.close()
    print("done")