# -*- coding: utf-8 -*-

# 이진 트리
'''
 작업중....
'''




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        print(node, end = ' ')
        if not node.left == None : self.preorder(node.left)
        if not node.right == None : self.preorder(node.right)


    def inorder(self, node):
        if not node.left == None : self.inorder(node.left)
        print(node, end = ' ')
        if not node.right == None : self.inorder(node.right)

    def postorder(self, node):
        if not node.left == None : self.postorder(node.left)
        if not node.right == None : self.postorder(node.right)
        print(node, end = ' ')
     

    def new_node(self, element):
        new = Node()
        new.data = element
        new.left = None
        new.right = None
        return new

    def search_node(self, node, element):
        if(node != None):
            if(node.data == element):
                return node
            else:
                tmp = self.search_node(node.left, element)
                if(tmp != None):
                    return tmp
                return self.search_node(node.right, element)

    def insert_node(self, node, A, B, C):
        node.data = A

        if(B != '.'): node.left = self.new_node(B)
        if(C != '.'): node.right = self.new_node(C)


        
        


if __name__ == "__main__":


    tree = Tree()
    N = int(input())
    for _ in range(N):
        node, left_node, right_node = map(Node, input().split())
        tmp = tree.search_node()
        

    
    print(       '전위 순회 : ', end='') ; tree.preorder(tree.root)
    print('\n' + '중위 순회 : ', end='') ; tree.inorder(tree.root)
    print('\n' + '후위 순회 : ', end='') ; tree.postorder(tree.root)