class TreeNode:
    def __init__(self, data, left=None, right=None):
        # Set the data value of the node
        self.data = data
        # Set the left child of the node
        self.left = left
        # Set the right child of the node
        self.right = right

    def __str__(self):
        # Return a string representation of the node
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        # Store the input data list
        self.data_lst = tree_data
        # Initialize the root node of the binary search tree as None
        self.tree = None
        # Initialize an empty list to store the values of the nodes in the tree
        self.values = []

    def data(self):
        for node in self.data_lst:
            # If the tree is empty
            if self.tree == None:
                # Create a new tree with the first node as the root
                self.tree = TreeNode(node)
            else:
                # Start from the root node
                current_node = self.tree
                # Flag to indicate if the last node has been found
                found_last_node = False
                # Loop until the last node is found
                while not found_last_node:
                    # If the node's data is less than or equal to the current node's data
                    if node <= current_node.data:
                        # If the current node doesn't have a left child
                        if current_node.left == None:
                            # Create a new left child with the given data
                            current_node.left = TreeNode(node)
                            # Found the last node, exit the loop
                            found_last_node = True
                        else:
                            # Move to the left child and continue traversing
                            current_node = current_node.left
                    else:
                        # If the node's data is greater than the current node's data
                        # If the current node doesn't have a right child
                        if current_node.right == None:
                            # Create a new right child with the given data
                            current_node.right = TreeNode(node)
                            # Found the last node, exit the loop
                            found_last_node = True
                        else:
                            # Move to the right child and continue traversing
                            current_node = current_node.right
            # Append the node's data to the list of values
            self.values.append(node)

        # Return the root of the constructed binary search tree
        return self.tree

    def sorted_data(self):
        # Build the binary search tree by calling the data() method
        self.data()
        # Return the sorted list of values in the tree
        return sorted(self.values)