class Node_order: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
def Inorder(root):   
    if root:    
        Inorder(root.left)    
        print(root.val),    
        Inorder(root.right) 
   
def Postorder(root):   
    if root:    
        Postorder(root.left)    
        Postorder(root.right)    
        print(root.val), 
   
def Preorder(root):   
    if root: 
        print(root.val),         
        Preorder(root.left)    
        Preorder(root.right) 

        
root = Node_order(1) 
root.left = Node_order(2) 
root.right = Node_order(3) 
root.left.left = Node_order(4) 
root.left.right = Node_order(5) 
print ("Preorder traversal is",Preorder(root))
print ("Inorder traversal is",Inorder(root))   
print ("Postorder traversal is",Postorder(root))
