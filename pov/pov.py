from json import dumps

class Tree:
    def __init__(self, label, children=None):
        # Initialize the tree node with a label (string) and optional children (a list of Tree instances)
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        # Return a dictionary representation of the tree
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        # Return a JSON-formatted string representation of the tree
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        # Compare two trees based on their labels
        return self.label < other.label

    def __eq__(self, other):
        # Check if two trees have the same structure and content
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        # Reorient the tree so that 'from_node' becomes the new root
        tree_dict = self.__dict__()

        # Get the new root node and the path to the original root
        try:
            new_root, path_to_original = self.get_node(tree_dict, from_node)
        except TypeError:
            raise ValueError("Tree could not be reoriented")

        # Reorganize parents along the path to create a new tree structure
        new_children = self.reorganize_parents(tree_dict, path_to_original, from_node)

        if new_children:
            new_root[from_node].append(new_children)

        # Create a new tree instance representing the reoriented tree
        tree_instance = self.create_tree(new_root)
        return tree_instance

    def path_to(self, from_node, to_node):
        # Find the path from 'from_node' to 'to_node' in the tree
        reoriented_tree = self.from_pov(from_node)
        reoriented_dict = reoriented_tree.__dict__()

        try:
            _, path = self.get_node(reoriented_dict, to_node)
        except TypeError:
            raise ValueError("No path found")

        return path + [to_node]

    def get_node(self, tree_dict, value, path=[]):
        # Recursively search for a node with the specified value
        if value in tree_dict.keys():
            return tree_dict, path

        if self.children:
            children_lst = list(tree_dict.values())[0]
            for child in children_lst:
                parent = list(tree_dict.keys())[0]
                updated_path = path + [parent]
                root_found = self.get_node(child, value, updated_path)
                if root_found:
                    return root_found

        return None

    def reorganize_parents(self, tree, path_to_original, from_node):
        # Reorganize parent-child relationships along the path to create a new tree structure
        skip_nodes = path_to_original + [from_node]
        node_lst = []

        for node in path_to_original:
            child, _ = self.get_node(tree, node)
            children_lst = [
                child_dict
                for child_dict in child[node]
                if list(child_dict.keys())[0] not in skip_nodes
            ]
            new_child = {node: children_lst}
            node_lst.append(new_child)

        if node_lst:
            temp_dict = dict()
            for n in node_lst:
                if not temp_dict:
                    temp_dict = n
                else:
                    label = list(n.keys())[0]
                    node = n
                    node[label].append(temp_dict)
                    temp_dict = node

            return temp_dict

        return None

    def create_tree(self, tree_dict):
        # Recursively create a new Tree instance based on the dictionary representation
        label = list(tree_dict.keys())[0]
        children = tree_dict[label]
        children_lst = []

        if children:
            for child in children:
                children_lst.append(self.create_tree(child))

        return Tree(label, children_lst)
