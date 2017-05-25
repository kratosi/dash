import os
import yaml
from node import Node

def get_all_yaml_files():
    curr_path = os.path.dirname(os.path.realpath(__file__))
    yaml_files = []
    for root, dirs, files in os.walk(os.path.join(curr_path, "trees")):
        for f in files:
            if f.endswith("full_binary.yaml"):
                yaml_files.append(os.path.join(root, f))
    return yaml_files


def create_tree_from_yaml(tree_yaml):
    def _get_root_val(tree_yaml):
        all_childs = []
        for k, v in tree_yaml.iteritems():
            if k in v:
                raise Exception("Node %s has itself as its child" % str(k))
            all_childs += v

        for k in tree_yaml.keys():
            if k not in all_childs:
                return k
        raise Exception("root not found")

    def _create_tree(root):
         if not root:
             return
         children = tree_yaml.get(root.data)

         # Dont do anything for leaf nodes
         if children:
             root.left = Node(children[0]) if children[0] else None
             root.right = Node(children[1]) if children[1] else None

             _create_tree(root.left)
             _create_tree(root.right)

    root_val = _get_root_val(tree_yaml)
    root = Node(root_val)

    _create_tree(root)
    return root

def load_all_trees():
    yaml_files = get_all_yaml_files()
    for yf in yaml_files:
        with open(yf, 'r') as f:
            try:
                tree_yaml = yaml.load(f)
                print tree_yaml
                return create_tree_from_yaml(tree_yaml)
                print "==========="
            except yaml.YAMLError as e:
                print "Failed to load file %s" % yf
                print e

def load_tree(yaml_file):
    curr_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(curr_path, "trees/" + yaml_file)
    if not os.path.exists(file_path):
        raise Exception("Yaml file %s not found" % yaml_file)
    with open(file_path, 'r') as f:
        try:
            tree_yaml = yaml.load(f)
            print tree_yaml
            return create_tree_from_yaml(tree_yaml)
        except yaml.YAMLError as e:
            print "Failed to load file %s" % file_path
            raise e


def inorder( node):
    if not node:
        return
    inorder(node.left)
    print node.data ,
    inorder(node.right)

#root = load_all_trees()
#inorder(root)
