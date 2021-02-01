"""完成堆栈的基本操作"""

class Stack(object):
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)

    def push(self, ite):
        self.item.append(ite)

    def pop(self):
        return self.item.pop()

if __name__ == "__main__":
    stack = Stack()
    stack.push("Guten Abend")
    stack.push("Herzlichen Willkommen")
    stack.push("Ich freue mich sehr")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
