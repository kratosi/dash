"""
Heap Property:
    - The value of the parent node is less than that of the child nodes (min heap)
    - The tree should be a complete binary tree. Because its complete there is no
      missing child from left to right and therefore array can be used to represent
      the tree

Min Value : O(1)
Insertion : Insert O(1) + Percolate up O(log n ) = O(log n)
deletion : Delete O(1) + Percolate down O(log n) = O(log n)
"""

class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def get_left_child_index(self, pindex):
        lci = pindex * 2 + 1
        if lci >= self.size:
            return -1
        return lci

    def get_right_child_index(self, pindex):
        rci = pindex * 2 + 2
        if rci >= self.size:
            return -1
        return rci

    def get_parent_index(self, cindex):
        return (cindex - 1)/2

    def insert(self, val):
        """ Add the value to the end of the heap.
        This causes heap imbalance. Then percolate_up from
        the last index, until the heap restores its property.
        """
        print "Inserting value: %d" % val
        self.heap.append(val)
        self.size += 1
        self.percolate_up(self.size - 1)
        #self.print_heap()

    def percolate_up(self, index):

        while index:
            pindex = self.get_parent_index(index)
            if self.heap[index] < self.heap[pindex]:
                self.heap[index], self.heap[pindex] = self.heap[pindex], self.heap[index]
            index = pindex

    def print_heap(self):
        print " , ".join([str(self.heap[v]) for v in range(self.size)])


    def get_min(self):
        """ Minimum is heap[0]
        To restore heap property replace this value with the last value and
        then percolate_down from that index
        """
        minv = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.percolate_down(0)
        self.print_heap()
        return minv

    def get_min_child_index(self, pindex):
        rchild = self.get_right_child_index(pindex)
        lchild = self.get_left_child_index(pindex)
        if lchild == -1 and rchild == -1:
            return -1
        elif lchild != -1 and rchild == -1:
            return lchild
        elif rchild != -1 and lchild == -1:
            return rchild
        elif self.heap[rchild] < self.heap[lchild]:
            return rchild
        else:
            return lchild

    def percolate_down(self, pindex):
        """ Get the minimum child and replace parent value with this value.
        Do this until the last child
        """

        while pindex != -1:
            child = self.get_min_child_index(pindex)
            if child != -1:
                if self.heap[pindex] > self.heap[child]:
                    self.heap[pindex], self.heap[child] = self.heap[child], self.heap[pindex]
            pindex = child

if __name__ == '__main__':
    h = Heap()
    inputs = [4, 3, 6, 8, 2 ,9, 6, 1]
    for i in inputs:
        h.insert(i)

    h.print_heap()

    print h.get_min()
    print h.get_min()
