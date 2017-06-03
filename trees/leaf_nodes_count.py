import util

def leaf_nodes_count(root):
    if not root:
        return 0
    # GO to the leaves and return 1 from them
    # sum it up to the root for both left and right trees

    if not root.left and not root.right:
        return 1

    ll = leaf_nodes_count(root.left)
    rl = leaf_nodes_count(root.right)

    return ll + rl

if __name__ == '__main__':
    root = util.load_tree('skew.yaml')
    print leaf_nodes_count(root)
    print
    #print root
    util.inorder(root)
