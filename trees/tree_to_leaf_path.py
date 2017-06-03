import util

def tree_to_leaf_path(root, path):
    if not root:
        return

    path.append(root.data)

    if not root.left and not root.right:
        print " ".join(path)
        return

    tree_to_leaf_path(root.left, path)
    # IMP:  because list is not part of stack we need to
    # manually delete the values which are pushed in the
    # previous recursive call.
    path.pop()
    tree_to_leaf_path(root.right, path)
    path.pop()

if __name__ == '__main__':
    root = util.load_tree('full_binary.yaml')
    print tree_to_leaf_path(root, [])
    #print root
    util.inorder(root)
