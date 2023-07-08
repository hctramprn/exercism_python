class Zipper:
    def __init__(self, tree, focus=[]):
        """
        Initializes a Zipper object with a given tree and an optional focus list.

        Args:
        - tree: The binary tree stored as nested dictionaries.
        - focus: A list representing the path from the root to the current node.

        """
        self.tree = tree
        self.focus = focus

    @staticmethod
    def from_tree(tree):
        """
        Static method that creates a Zipper object from a given tree.

        Args:
        - tree: The binary tree stored as nested dictionaries.

        Returns:
        - Zipper: A new Zipper object.

        """
        return Zipper(tree)

    def value(self):
        """
        Returns the value of the current node in the zipper.

        Returns:
        - Any: The value of the current node.

        """
        return self.tree['value']

    def set_value(self, value):
        """
        Sets the value of the current node in the zipper to the given value.

        Args:
        - value: The new value for the current node.

        Returns:
        - Zipper: A new Zipper object with the updated value.

        """
        if self.focus:
            tree = self.focus[0][0]
        else:
            tree = self.tree
        nested_dict = tree
        directions_lst = [dir for _, dir in self.focus]
        for direction in directions_lst:
            nested_dict = nested_dict[direction]
        nested_dict['value'] = value
        return Zipper(tree)

    def left(self):
        """
        Returns a new Zipper object representing the left child of the current node.

        Returns:
        - Zipper or None: The Zipper object for the left child, or None if it doesn't exist.

        """
        if self.tree['left'] is None:
            return None
        return Zipper(self.tree['left'], self.focus + [(self.tree, 'left')])

    def set_left(self, leaf):
        """
        Sets the left child of the current node to the given leaf value.

        Args:
        - leaf: The value to be assigned as the left child.

        Returns:
        - Zipper: A new Zipper object with the updated left child.

        """
        if self.focus:
            tree = self.focus[0][0]
        else:
            tree = self.tree
        nested_dict = tree
        directions_lst = [dir for _, dir in self.focus]
        for direction in directions_lst:
            nested_dict = nested_dict[direction]
        nested_dict['left'] = leaf
        return Zipper(tree)

    def right(self):
        """
        Returns a new Zipper object representing the right child of the current node.

        Returns:
        - Zipper or None: The Zipper object for the right child, or None if it doesn't exist.

        """
        if self.tree['right'] is None:
            return None
        return Zipper(self.tree['right'], self.focus + [(self.tree, 'right')])

    def set_right(self, leaf):
        """
        Sets the right child of the current node to the given leaf value.

        Args:
        - leaf: The value to be assigned as the right child.

        Returns:
        - Zipper: A new Zipper object with the updated right child.

        """
        if self.focus:
            tree = self.focus[0][0]
        else:
            tree = self.tree
        nested_dict = tree
        directions_lst = [dir for _, dir in self.focus]
        for direction in directions_lst:
            nested_dict = nested_dict[direction]
        nested_dict['right'] = leaf
        return Zipper(tree)

    def up(self):
        """
        Returns a new Zipper object representing the parent of the current node.

        Returns:
        - Zipper or None: The Zipper object for the parent, or None if it is the root.

        """
        if not self.focus:
            return None
        parent = self.focus[-1][0]
        return Zipper(parent, self.focus[:-1])

    def to_tree(self):
        """
        Returns the original tree from which the zipper was created.

        Returns:
        - dict: The original binary tree stored as nested dictionaries.

        """
        if not self.focus:
            return self.tree
        initial_tree, direction = self.focus[0]
        return initial_tree
