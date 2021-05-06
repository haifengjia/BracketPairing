import os
from pathconf import proj_path, json_path
import json


class Stack:
    def __init__(self):
        self.lista = []  # 创建空栈

    def get_len(self):
        return len(self.lista)

    def isEmpty(self):
        return len(self.lista) == 0

    def push(self, item):
        self.lista.append(item)

    def pop(self):
        if self.isEmpty():
            return "Error：The stack is empty"
        else:
            return self.lista.pop()

    def getBot(self):
        if self.isEmpty():
            return "Error：The stack is empty"
        else:
            return self.lista[0]

    def delist(self):
        if self.isEmpty():
            return "Error：The stack is empty"
        else:
            return self.lista.pop(0)


def pairing(fileList, left='(', right=')'):
    pos = 0
    i = 0
    res = []
    L = []
    R = []
    maxDepth = 0
    brkStk = Stack()
    for line in fileList:
        i += 1
        j = 0
        for c in line:
            j += 1
            if c == left:
                brkStk.push((i, j))
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
            maxDepth = max(maxDepth, brkStk.get_len())

    # check unpaired left bracktes
    if not brkStk.isEmpty():
        while not brkStk.isEmpty():
            pos = L.index(brkStk.getBot())
            R.insert(pos, (-1, -1))
            brkStk.delist()
    else:
        pass

    res = [L, R]
    return (maxDepth, res)


if __name__ == '__main__':
    # file input
    # fileName = input()
    if proj_path[-1] != '/':
        proj_path = proj_path + "/"  # NOTE: ensure that the path is openable!!!

    files = os.listdir(proj_path+"src/")
    resDict = []
    for file in files:
        f = open(proj_path + "src/" + file, 'r')
        content = f.readlines()
        resList = pairing(content, '(', ')')
        isPaired = (not (-1, -1) in resList[1][0]
                    ) and (not (-1, -1) in resList[1][1])
        resDict.append({
            "File name": file, "Maximum depth": resList[0], "isPaired": isPaired})
        f.close()
    with open(os.path.abspath("..") + json_path, 'w') as resFile:
        json.dump(resDict, resFile, indent=1)
