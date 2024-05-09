class  Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
class Tree:
    def createNode(self,data):
        return Node(data)
