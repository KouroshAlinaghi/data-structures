import sys
import re

class Queue:
    def __init__(self):
        self.data = list()

    def getSize(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.insert(0, value)

    def dequeue(self):
        tmp = self.data[-1]
        self.data.pop()
        return tmp

    def isEmpty(self):
        return len(self.data) == 0

    def getInOneLine(self):
        return " ".join(reversed(self.data))


class Stack:
    def __init__(self, size=10):
        self.cap = size
        self.data = list()

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, value):
        self.data.append(value)

    def pop(self):
        tmp = self.peek()
        self.data.pop()
        return tmp

    def put(self, value):
        self.data.pop()
        self.push(value)

    def peek(self):
        return self.data[-1]

    def expand(self):
        self.cap *= 2

    def getInOneLine(self):
        return " ".join(self.data)

    def getSize(self):
        return len(self.data)

    def getCapacity(self):
        return self.cap

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def getList(self):
        cur = self.head
        s = ""
        while cur:
            s += str(cur.value) + " "
            cur = cur.next
        return s

    def insertFront(self, new_data):
        if self.head == None:
            self.head = Node(new_data)
        else:
            node = Node(new_data)
            tmp = self.head
            self.head = node
            node.next = tmp

    def insertEnd(self, new_data):
        cur = self.head
        if cur == None:
            self.head = Node(new_data)
        else:
            while cur.next:
                cur = cur.next
            node = Node(new_data)
            cur.next = node

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        self.head = prev


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
