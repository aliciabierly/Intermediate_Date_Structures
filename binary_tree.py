class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        '''The insert method will insert a new item into the tree. It will do so by creating
        a new node with the given integer then adding it to the tree. This should also preserve the
        ordering requirement that all nodes on the right side of a subtree are greater than the value
        in the root of that subtree, and all elements on the left side are lesser than the value in the
        root of the subtree'''
        self.root = self.insert_helper(self.root, value)
    
    def insert_helper(self, node, value):
        if node is None:
            return TreeNode(value)
        
        if value < node.value:
            node.left = self.insert_helper(node.left, value)
        else:
            node.right = self.insert_helper(node.right, value)
        
        return node
    
    def find_min(self, node):
        while node.left != None:
            node = node.left
        return node
    
    def delete_helper(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self.delete_helper(node.left, value)
        elif value > node.value:
            node.right = self.delete_helper(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                right_min = self.find_min(node.right)
                node.value = right_min.value
                node.right = self.delete_helper(node.right, right_min.value)
        return node

    def delete(self, value):
        '''remove a node from the tree with the given value and return it'''
        self.root = self.delete_helper(self.root, value)

    def find_helper(self, node, value):
        if node is None:
            return False
    
        if value < node.value:
            return self.find_helper(node.left, value) 
        elif value > node.value:
            return self.find_helper(node.right, value) 
    
        if value == node.value:
            return True
        #return False
        
    def find(self, value):
        return self.find_helper(self.root, value)

    def inorder_traversal(self):
        output_list = []
        self.inorder_helper(self.root, output_list)
        return output_list
    
    def inorder_helper(self, node, output_list):
        if node != None:
            self.inorder_helper(node.left, output_list)
            output_list.append(node.value)
            self.inorder_helper(node.right, output_list)