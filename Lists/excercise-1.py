'''
Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. So middle([1,2,3,4]) should return [2,3].
'''


def middle(input_list):
    x = input_list[1:-1]
    print(x)
    return input_list


middle([1, 2, 3, 4])
