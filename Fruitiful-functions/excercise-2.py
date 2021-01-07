'''
Exercise 6.5 The Ackermann function, A(m, n), is defined:
Write a function named ack that evaluates Ackerman's function. Use your
function to evaluate ack(3, 4), which should be 125. What happens for larger
values of m and n?
'''
m = 3
n = 4

def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        print('hello')
        return ack(m - 1, ack(m, n - 1))


ack(3, 4)