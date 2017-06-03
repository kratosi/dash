

import util

def similar(root1, root2):
    if not root1 and not root2:
        return True

    if (root1 and not root2 ) or (root2 and not root1):
        return False

    if root1.data != root2.data:
        return False

    sl = similar(root1.left, root2.left)
    if not sl:
        return False
    return similar(root1.right, root2.right)

if __name__ == '__main__':
    root1 = util.load_tree('full_binary.yaml')
    root2 = util.load_tree('full_binary.yaml')
    print similar(root1, root2)
    #print root
    util.inorder(root1)
