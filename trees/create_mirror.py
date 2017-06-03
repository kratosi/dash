import util

def create_mirror(root):
    if not root:
        return
    # Root tell its children that you both go and create your
    # mirrors and then give me refs. I will swap you too
    # after you are done
    lt = create_mirror(root.left)
    rt = create_mirror(root.right)

    root.left = rt
    root.right = lt
    return root

if __name__ == '__main__':
    root = util.load_tree('full_binary.yaml')
    util.inorder(root)
    nroot = create_mirror(root)
    print
    #print root
    util.inorder(nroot)
