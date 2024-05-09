class  Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
class Tree:
    def createNode(self,data):
        return Node(data)
    def insert(self,node,data):
        if(node is None):
            return self.createNode(data)
        if(data<node.data):
            node.left= self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    def inorderTraversal(self,root):
        if(root is not None):
            self.inorderTraversal(root.left)
            print(root.data)
            self.inorderTraversal(root.right)
        
tree=Tree()
root=tree.createNode(5)
# tree.insert(root,5)
tree.insert(root,8)
tree.insert(root,9)
tree.insert(root,1)
tree.insert(root,2)
tree.insert(root,55)
tree.insert(root,7)
tree.insert(root,3)
tree.insert(root,35)
tree.insert(root,56)
tree.insert(root,75)
tree.insert(root,87)
tree.insert(root,85)

print("INORDER TRAVERSAL:-")
tree.inorderTraversal(root)