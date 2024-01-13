class Bst:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = self.Node(key)
            return self.root
        return self.insert_rec(self.root, key)
    
    def insert_rec(self, node, value):
        if value >= node.value:
            if node.right == None:
                node.right = self.Node(value)
                node.right.parent = node
                return node.right
            else:
                return self.insert_rec(node.right, value)
        else:
            if node.left == None:
                node.left = self.Node(value)
                node.left.parent = node
                return node.left
            else:
                return self.insert_rec(node.left, value)

    def get_height(self, cur, node, h):
        if cur == node:
            return h
        if node.value >= cur.value:
            return self.get_height(cur.right, node, h + 1)
        else:
            return self.get_height(cur.left, node, h + 1)

bst = Bst()
n = int(input())
a = [int(x) for x in input().split()]
nodes = list()
for i in range(len(a)):
    node = bst.insert(a[i])
    nodes.append(node)
    if i:
        print(node.parent.value, end = " ")
print()

a, b = [int(x) for x in input().split()]
a = nodes[a - 1]
b = nodes[b - 1]

h_a = bst.get_height(bst.root, a, 0)
h_b = bst.get_height(bst.root, b, 0)

if h_a > h_b:
    for _ in range(h_a - h_b):
        a = a.parent
else:
    for _ in range(h_b - h_a):
        b = b.parent

while a != b:
    a = a.parent
    b = b.parent

for i in range(len(nodes)):
    if nodes[i] == a:
        print(i + 1)
        exit(0)
