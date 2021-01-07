'''
Write a function called remove_duplicates that takes a list and returns a new
list with only the unique elements from the original.
'''


# def remove_duplicates(input_list):
#     sorted_list = input_list[:]
#     sorted_list.sort()
#     for i in range(len(sorted_list)-1):
#         if sorted_list[i] == sorted_list[i+1]:
#             del sorted_list[i]
#     return sorted_list


def remove_duplicates(t):
    x = []
    for a in t:
        if a not in x:
            x.append(a)
    return x

    
print(remove_duplicates([1, 2, 3, 4, 4, 5, 5, 7, 7, 10]))
