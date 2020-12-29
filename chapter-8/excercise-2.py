'''
Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None
'''


def chop(list_elements):
    del list_elements[0]
    del list_elements[-1]


my_list = [1, 2, 3, 4]
chop_list = chop(my_list)
print(my_list)                          
print(chop_list) 
