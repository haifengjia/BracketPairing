# ETHAN JIA 2021/04/11
from Stack import Stack


def pairing(fileList, row, col, left='(', right=')'):
    pos = 0
    i = j = 0
    brkStk = Stack()
    for line in fileList:
        # print(line)
        i += 1
        for c in line:
            # print(c)
            j += 1
            if c == left:
                brkStk.push(j)


if __name__ == '__main__':
    # file input
    fileName = input()
    # print(fileName)
    fileList = open(fileName, 'r')
    content = fileList.readlines()
    # print(content)
    pairing(content, 1, 1, '(', ')')
