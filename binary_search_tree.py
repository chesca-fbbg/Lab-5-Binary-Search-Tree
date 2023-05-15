from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): 
        # Returns empty BST
        self.root = None

    def is_empty(self): 
        # returns True if tree is empty, else False
        if self.root == None:
            return True
        return False

    def search(self, key): 
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        def rec(node, k):
            if node.key == k:
                return True
            elif node.key > k:
                if node.left == None:
                    return False
                else:
                    return rec(node.left, k)
            else: 
                if node.right == None:
                    return False
                else:
                    return rec(node.right, k)
        return rec(self.root, key)

    def insert(self, key, data=None): 
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        n = TreeNode(key, data)
        if self.root == None:
            self.root = n
        def rec(node, k, d):
            if node.key == k:
                node = n
            elif node.key > k:
                if node.left == None:
                    node.left = n
                else:
                    rec(node.left, k, d)
            else:
                if node.right == None:
                    node.right = n
                else:
                    rec(node.right, k, d)
        rec(self.root, key, data)

    def find_min(self): 
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root == None:
            return None
        def rec(node):
            if node.left == None:
                return (node.key, node.data)
            else:
                return rec(node.left)
        return rec(self.root)

    def find_max(self): 
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root == None:
            return None
        def rec(node):
            if node.right == None:
                return (node.key, node.data)
            else:
                return rec(node.right)
        return rec(self.root)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root == None:
            return None
        def rec(node):
            if node.left != None:
                left = rec(node.left)
            else:
                left = 0
            if node.right != None:
                right = rec(node.right)
            else: right = 0
            return max(left, right) + 1
        return rec(self.root)

    def inorder_list(self): 
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root == None:
            return []
        l = []
        def rec(node):
            if node.left == None:
                l.append(node.key)
                if node.right != None:
                    rec(node.right)
            else:
                rec(node.left)
                l.append(node.key)
                if node.right != None:
                    rec(node.right)
        rec(self.root)
        return l

    def preorder_list(self):  
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root == None:
            return []
        l = []
        def rec(node):
            l.append(node.key)
            if node.left != None:
                rec(node.left)
            if node.right != None:
                rec(node.right)
        rec(self.root)
        return l
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000) # Don't change this!
        if self.root == None:
            return []
        l = []
        q = Queue(25000)
        q.enqueue(self.root)
        while q.size() > 0:
            l.append(q.items[q.front].key)
            if q.items[q.front].left != None:
                q.enqueue(q.items[q.front].left)
            if q.items[q.front].right != None:
                q.enqueue(q.items[q.front].right)
            q.dequeue()
        return l
        

