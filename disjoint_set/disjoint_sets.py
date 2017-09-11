
class Node:
    def __init__(self, data):
        self.parent = self
        self.data = data
        self.rank = 0

class DisjointSet():
    def __init__(self):
        self.sets = {}

    def make_set(self, data):
        self.sets[data] = Node(data)

    def union(self, data1 , data2):
        # This return the parent after doing path compression.
        # This is important because if we dont do find before the comparison
        # then we will get wrong parents
        parent1 = self.find_set(data1)
        parent2 = self.find_set(data2)

        # if both the parents are same then they are in same set
        if parent1.data == parent2.data:
            return False

        # compare the ranks of the node 1 parent and node 2 parent.
        # If node 1 parent rank is more then make node1 as parent of node2 else vice-versa
        # if both are ranks are equal then make node1 as parent of node2 and
        # increment the rank of node1 by 1

        # Change the parent references
        if parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2
        return True

    def find_set(self, data):
        """ This returns the set representative aka root of the tree.
        If the data node is not a direct child of root then this does path
        compression and makes all the nodes in the path from the node to the
        root as direct child of the root so that the height of the tree is
        reduced.
        """
        node = self.sets[data]
        if node.parent == node:
            return node
        else:
            # This is path compression
            # Make all the nodes in the path from the node to the
            # parent directly attached to the parent
            node.parent = self.find_set(node.parent.data)
            return node.parent



if __name__ == '__main__':
    d = DisjointSet()

    inputs = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for i in inputs:
        d.make_set(i)

    print d.sets['C'].parent
    print d.sets['C'].data

    d.union('A', 'B')
    d.union('C', 'D')
    print d.sets['D'].parent.data
    d.union('A', 'C')
    print d.sets['D'].parent.data
    print d.find_set('D').data
    print d.sets['D'].parent.data
