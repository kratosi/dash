from node import Node

class BST(object):
    def __init__(self):
        self.root = None

    def pprint(self, node):
        if not node:
            return
        self.pprint(node.left)
        print node.data ,
        self.pprint (node.right)

    def insert(self, data):
        """
         Insert in a Bst
         check if new data is less than root data
           - if yes then check if left child exists
             - if yes then move to left child
             - if no insert node here and return
           - if no i.e. new data is more the root data
             - check if root right exists
                - if yes move to right child
                - if no insert here and return
        """
        node = Node(data)
        if not self.root:
            self.root = node
            return

        cur = self.root
        while cur:
            if data < cur.data:
                # Check if there is no left node.
                # In not then insert the node here
                if not cur.left:
                    cur.left = node
                    return
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = node
                    return
                cur = cur.right


if __name__ == '__main__':
    t = BST()
    inputs = [3, 4, 5, 4, 6, 1, 10, 2]
    for i in inputs:
        t.insert(i)
    t.pprint(t.root)
