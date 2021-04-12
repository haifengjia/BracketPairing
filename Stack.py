class Stack:
    def __init__(self):
        self.lista = []  # 创建空栈

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
