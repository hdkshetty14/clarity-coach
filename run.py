import os

def print_structure(base_dir, level=0, max_depth=2):
    if level > max_depth:
        return
    for item in os.listdir(base_dir):
        path = os.path.join(base_dir, item)
        indent = "    " * level
        if os.path.isdir(path):
            print("{}📁 {}".format(indent, item))
            print_structure(path, level + 1, max_depth)
        else:
            print("{}📄 {}".format(indent, item))

print_structure(".")
