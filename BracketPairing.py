# ETHAN JIA 2021/04/11
from Stack import Stack


def pairing(fileList, row, col, left='(', right=')'):
    # FIXME: add the first row/col to start
    pos = 0
    i = 0
    res = []
    L = []
    R = []
    brkStk = Stack()
    for line in fileList:
        # print(line)
        i += 1
        j = 0
        for c in line:
            # print(c)
            j += 1
            if c == left:
                brkStk.push(c)
                L.append((i, j))
            elif c == right:
                if not brkStk.isEmpty():
                    R.append((i, j))
                    brkStk.pop()
                else:
                    L.append((-1, -1))
                    R.append((i, j))
                    continue
            else:
                continue
    res = [L, R]
    return res


if __name__ == '__main__':
    # file input
    fileName = input()
    # print(fileName)
    fileList = open(fileName, 'r')
    content = fileList.readlines()
    # print(content)
    l = pairing(content, 1, 1, '(', ')')
    print(l)
