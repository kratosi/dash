#
# diameter of a tree is the maximum( maximum(left diameter, right diamter),
#                                     (left_height + right_height +1))
#            A
#          /  \
#         E   F
#        / \
#       C   D
#      /     \
#     B       Z
#    /         \
#   X           R
#
#  Diameter of this tree is X-B-C-E-D-Z-R

import util

def height(root):
    """ Height of root is max( height of left subtree,
                               height of right subtree) + 1
    """
    if not root:
        return 0
    hl = height(root.left)
    hr = height(root.right)
    return 1 + max(hl, hr)


def diameter(root, path):
    """ I am root , my diameter is either my diameter ( lh + rh + 1) or
        if any other subtree has a bigger diameter
    """
    # diameter of a null tree is 0
    if not root:
        return 0

    left_tree_diameter = diameter(root.left, path)
    right_tree_diameter = diameter(root.right, path)

    hl = height(root.left)
    hr = height(root.right)

    if (hl + hr + 1) > max(left_tree_diameter, right_tree_diameter):
        path.append(root.data)
    return max(max(left_tree_diameter, right_tree_diameter), (hl + hr + 1))

if __name__ == '__main__':
    root = util.load_tree('diameter.yaml')
    path = []
    print diameter(root, path)
    print "path" ,path
    #print root
    util.inorder(root)
