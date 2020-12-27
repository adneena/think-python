'''
This exercise can be done using only the statements and other features we have learned
so far.
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence:
print '+', '-'
If the sequence ends with a comma, Python leaves the line unfinished, so the value printed
next appears on the same line.
print '+',
print '-'
The output of these statements is '+ -'.
A print statement all by itself ends the current line and goes to the next line.
'''


def do_Func(function, val, iter):
    i=0 
    while i < iter:
        function(val)
        i=i+1


def printer(val):
    print(val)


colCell = '+ - - - - + - - - - +'
rowCell = '|         |         |'

do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)