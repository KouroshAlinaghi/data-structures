import sys
import re

INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'

class MinHeap:
    def __init__(self):
        self.data = []

    def bubble_up(self, index):
        self.check_index(index)
        if index == 0:
            return
        parent = (index + 1) // 2 - 1
        if self.data[index] < self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            self.bubble_up(parent)

    def bubble_down(self, index):
        self.check_index(index)
        l = (index + 1) * 2 - 1
        r = (index + 1) * 2

        if len(self.data) - 1 < l:
            return

        if len(self.data) - 1 == l:
            if self.data[l] < self.data[index]:
                self.data[index], self.data[l] = self.data[l], self.data[index]
            return

        if self.data[index] > min(self.data[l], self.data[r]):
            index_to_be_swapped = l if self.data[l] < self.data[r] else r
            self.data[index], self.data[index_to_be_swapped] = self.data[index_to_be_swapped], self.data[index]
            self.bubble_down(index_to_be_swapped)

    def heap_push(self, value):
        self.data.append(value)
        self.bubble_up(len(self.data) - 1)

    def heap_pop(self):
        if len(self.data) == 0:
            raise Exception("empty")
        self.data[-1], self.data[0] = self.data[0], self.data[-1]
        x = self.data[-1]
        self.data.pop()
        if len(self.data) > 0:
            self.bubble_down(0)
        return x

    def find_min_child(self, index):
        self.check_index(index)
        l = (index + 1) * 2 - 1
        r = (index + 1) * 2
        if l > len(self.data) - 1:
            return -1
        return r if self.data[l] > self.data[r] else l

    def heapify(self, *args):
        for x in args:
            self.heap_push(x)

    def check_index(self, index):
        if not isinstance(index, int):
            raise Exception("invalid index")
        if index > len(self.data) - 1 or index < 0:
            raise Exception("out of range index")


class HuffmanTree:
    class Node:
        def __init__(self, repeats, char, left = None, right = None):
            self.repeats = repeats
            self.char = char
            self.left = left
            self.right = right

        def __gt__(self, other):
            return self.repeats > other.repeats

        def __lt__(self, other):
            return self.repeats < other.repeats

    def __init__(self):
        self.root = None
        self.data = str()
        self.letters = list()
        self.repeats = list()

    def set_letters(self, *args):
        self.letters = list(args)

    def set_repetitions(self, *args):
        self.repeats = list(args)
        for i in range(len(self.letters)):
            self.data += self.repeats[i] * self.letters[i]

    def dfs(self, codes, node, code):
        if node.left == None:
            codes[node.char] = code
            return

        self.dfs(codes, node.left, code + "0")
        self.dfs(codes, node.right, code + "1")

    def build_huffman_tree(self):
        heap = MinHeap()
        for i in range(len(self.letters)):
            heap.heap_push(self.Node(self.repeats[i], self.letters[i]))

        while len(heap.data) > 1:
            l, r = heap.heap_pop(), heap.heap_pop()
            parent = self.Node(l.repeats + r.repeats, "meow", l, r)
            heap.heap_push(parent)
            self.root = parent

    def get_huffman_code_cost(self):
        codes = dict()
        self.dfs(codes, self.root, "")
        ans = 0
        for i in range(len(self.letters)):
            ans += self.repeats[i] * len(codes[self.letters[i]])
        return ans


    def text_encoding(self, text):
        self.data = text
        text = list(set(text))
        text.sort()
        self.letters = text
        for c in text:
            self.repeats.append(list(self.data).count(c))
        self.build_huffman_tree()


class Bst:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = self.Node(key)
            return
        self.insert_rec(self.root, key)
    
    def insert_rec(self, node, value):
        if value > node.value and node.right == None:
            node.right = self.Node(value)
            return
        if value < node.value and node.left == None:
            node.left = self.Node(value)
            return

        if value > node.value:
            self.insert_rec(node.right, value)
        else:
            self.insert_rec(node.left, value)

    def inorder(self):
        self.inorder_rec(self.root)
        print()

    def inorder_rec(self, node):
        if node == None:
            return
        self.inorder_rec(node.left)
        print(node.value, end=' ')
        self.inorder_rec(node.right)


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

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

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
