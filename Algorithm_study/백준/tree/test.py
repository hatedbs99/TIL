def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(3)
    preorder(4)

node = {1 : '.'}

preorder(node)