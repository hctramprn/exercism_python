class Node:
    # inits the node object with the given values
    def __init__(self, value, succeeding=None, previous=None):
        self.data = value
        self.succeeding = succeeding
        self.previous = previous

    # returns the node's value
    def value(self):
        return self.data

    # returns the next node
    def next(self):
        return self.succeeding

    # returns the previous node
    def prev(self):
        return self.previous


class LinkedList:
    # inits the linked list with no succeeding or previous nodes
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # pushes a new node at the back of the linked list
    def push(self, value):
        # if a node is already present, creates a new node
        # with the previous head as the current's succeeding node value.
        # Also, it updates the previous node value with the new node
        if self.length:
            node = Node(value, succeeding=self.head)
            self.head.previous = node
        # else, creates a new node with no succeeding or previous nodes
        else:
            node = Node(value)

        # if there's no tail, saves this node as the tail of the list
        if not self.tail:
            self.tail = node

        # updates the new head and length values
        self.head = node
        self.length += 1
        return

    def pop(self):
        # if the list has nodes, gets the next node value
        # and stores it as the new list's head.
        # Then it substracts a node from the length and
        # returns the node's value
        if self.length:
            node = self.head
            self.head = node.next()
            self.length -= 1
            return node.value()
        # raises an IndexError if the pop function is
        # called on an empty list
        else:
            raise IndexError('List is empty')

    def shift(self):
        # if the list has nodes, reassigns the tail of the list
        # to the previous node of the current tail.
        # Then it substracts a node from the length and returns
        # the value of the previous tail.
        if self.length:
            node = self.tail
            self.tail = node.prev()
            self.length -= 1
            return node.value()
        # else, raises an IndexError if the shift function
        # is called on an empty list
        else:
            raise IndexError('List is empty')

    def unshift(self, value):
        # if a node is already present, creates a new node
        # with the previous tail as the current's previous node value.
        # Also, it updates the succeeding node value with the new node
        if self.length:
            node = Node(value, previous=self.tail)
            self.tail.succeeding = node
        # else, creates a new node with no succeeding or previous nodes
        # and assigns this node as the new head
        else:
            node = Node(value)
            self.head = node

        # assigns this node as the list's tail and adds a
        # node to the length
        self.tail = node
        self.length += 1
        return

    def __len__(self):
        # returns the list's length
        return self.length

    def delete(self, value):
        # if a node is already present, sets the current
        # head as the start of the search and delete
        if self.length:
            node = self.head
            # while the node has a value compare it with the given value
            while node.data:
                if node.data == value:
                    # if found, sets the head, tail or previous and
                    # succeeding values depending on the position
                    # of the node
                    if node == self.head:
                        self.head = node.succeeding
                    elif node == self.tail:
                        self.tail = node.previous
                    else:
                        node.previous.succeeding = node.succeeding
                        node.succeeding.previous = node.previous
                    # substracts a node from the length and returns it value
                    self.length -= 1
                    return node.value()

                # if there's no next node, raises a ValueError exception
                if node.succeeding == None:
                    raise ValueError('Value not found')
                # else, repeats the process with the next node
                else:
                    node = node.next()
        # if the function is called on an empty list,
        # raises a ValueError exception
        else:
            raise ValueError('Value not found')
