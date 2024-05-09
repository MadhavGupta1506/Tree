class  Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
class Tree:
    def createNode(self,data):
        return Node(data)
    def insert(self,node,data):
        if(node==None):
            return self.createNode(data)
        if(node<node):
            return self.insert(node.left,data)
        else:
            return self.insert(node.right,data)
        