def tree_from_traversals(preorder, inorder):
    # Create sets of unique elements from the traversals
    preorder_set = set(preorder)
    inorder_set = set(inorder)

    # Check if the lengths of traversals are equal
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    # Check if the sorted traversals have the same elements
    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")

    # Check if traversals contain unique items
    if len(preorder) != len(preorder_set) or len(inorder) != len(inorder_set):
        raise ValueError("traversals must contain unique items")

    # Check if both traversals are empty, indicating the end of a subtree
    if not preorder and not inorder:
        return dict()

    # Take the first element from preorder as the root of the tree
    root = preorder[0]

    # Find the index of the root in the inorder traversal
    root_index = inorder.index(root)

    # Divide the inorder traversal into left and right subtrees based on the root index
    left_subtree = inorder[:root_index]
    right_subtree = inorder[root_index + 1:]

    # Create the corresponding left and right preorder traversals
    left_preorder = preorder[1:len(left_subtree) + 1]
    right_preorder = preorder[len(left_subtree) + 1:]

    # Initialize a dictionary for the tree with the root and empty left and right subtrees
    tree = {'v': root, 'l': dict(), 'r': dict()}

    # Recursively construct the left subtree
    if left_subtree:
        tree['l'] = tree_from_traversals(left_preorder, left_subtree)

    # Recursively construct the right subtree
    if right_subtree:
        tree['r'] = tree_from_traversals(right_preorder, right_subtree)

    # Return the constructed tree
    return tree
