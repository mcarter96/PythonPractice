# June 11
# Given a binary search tree, print out the elements of the tree in order without using recursion 
# Problem source: https://www.byte-by-byte.com/inordertraversal/
#     5
#    / \
#   2   7
#  / \ / \
# 1  3 6  8     

class Node:

    # Initializes a node
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Creates the binary tree
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # in order traversal using recursion
    def inOrderRecur(self, root):
        traversal = []
        if root:
            traversal = self.inOrderRecur(root.left)
            traversal.append(root.data)
            traversal = traversal + self.inOrderRecur(root.right)
        return traversal

    # in order traversal without recursion
    def inOrder(self, root):
        current = root
        subtree = []
        tree = []

        while True:
            if current is not None:
                subtree.append(current)
                current = current.left
            elif subtree:
                current = subtree.pop()
                tree.append(current.data)
                current = current.right
            else:
                break
        return tree

        
def main():
    root = Node(5)
    root.insert(1)
    root.insert(2)
    root.insert(3)
    root.insert(7)
    root.insert(8)
    root.insert(6)
    print(root.inOrderRecur(root))
    print(root.inOrder(root))

if __name__ == "__main__":
    main()
