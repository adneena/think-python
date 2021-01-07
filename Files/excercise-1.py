import os


def sed(pattern, replacement, fin, fout):
    # Open File One
    finMem = open(fin)

    # Write Contents to File Two
    foutMem = open(fout, 'w+')

    # Search and replace string
    for line in finMem:
        if pattern in line:
            print('pattern found')
            # Don't think it's possible to use list = list.replace()
            # TODO Investigate further
            newLine = line.replace(pattern, replacement)
            foutMem.write(newLine)
        else:
            foutMem.write(line)


if __name__ == '__main__':
    print(os.getcwd())
    pattern = 'oy'
    replacement = 'it'
    fin = r"C:\Users\Aradh\Documents\wow.txt"
    fout = r"C:\Users\Aradh\Documents\nextwow.txt"
    sed(pattern, replacement, fin, fout)