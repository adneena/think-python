'''
1. Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.
2. If there are 23 students in your class, what are the chances that two of you have the same
birthday? You can estimate this probability by generating random samples of 23 birthdays and
checking for matches. Hint: you can generate random birthdays with the randint function
in the random module
'''
import random


def has_duplicates(input_list):
    sorted_list = input_list[:]
    sorted_list.sort()
    # sorted_list = input_list.sort()
    for i in range(len(sorted_list)-1):
        if sorted_list[i] == sorted_list[i+1]:
            return True


print(has_duplicates([1, 2, 5, 6, 7]))


def birthday_duplicates():
    birthdays = []
    count = 0
    i = 0
    while i < 1000:
        for items in range(23):
            birthdays.append(random.randint(1,365))

        if has_duplicates(birthdays):
            count += 1
        i = i+1
    return count/i * 100
