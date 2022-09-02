class Node:
    def __init__(self, val, left=None, right=None, __flag='empty'):
        self.val = val
        self.left = left
        self.right = right
        self.__flag = __flag

    def __getitem__(self, item):
        if item == 0:
            return self.val
        elif item == 1:
            return self.left
        elif item == 2:
            return self.right
        else:
            raise Exception('Out of range (0..2!')

    def __repr__(self):
        return repr((self.val, self.left, self.right))

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if isinstance(val, str):
            raise Exception('Value could not be str!')
        if self.root == None:
            self.root = Node(val)
        else:
            __cache=[]
            __cache.append(self.root)
            self.__add(val, self.root, __cache)

    def __add(self, val, node, __cache):
        if node._Node__flag == 'empty':
            if node.left == None:
                node.left = Node(val)
                node._Node__flag = 'left'
            else:
                __cache.append(node.left)
                self.__add(val, node.left, __cache)
        elif node._Node__flag == 'left':
            if node.right == None:
                node.right = Node(val)
                node._Node__flag = 'filled'
                self.__back_prop(__cache)
            else:
                __cache.append(node.right)
                self.__add(val, node.right, __cache)
        else:
            node._Node__flag = 'empty'
            __cache.append(node.left)
            self.__add(val, node.left, __cache)

    def __back_prop(self, __cache):
        priv = __cache[-1]
        __cache = __cache[:-1]
        if priv._Node__flag == 'empty':
            priv._Node__flag = 'left'
            return
        elif priv._Node__flag == 'left':
            priv._Node__flag = 'filled'
        if len(__cache) != 0:
            self.__back_prop(__cache)

    def __getitem__(self, item):
        return self.root[item]

    def __repr__(self):
        return repr(self.root)
