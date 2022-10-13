class Node:
    ''' Declares the initial values of the node.
        It stores the value passed and the reference
        to the next node. If there is no next node,
        will get the value None
    '''
    def __init__(self, value, next_node):
        self.data = value
        self.next_node = next_node

    # returns the value passed
    def value(self):
        return self.data

    # returns the reference to the next node or null for empty lists
    def next(self):
        return self.next_node


class LinkedList:
    # creates the linked list object with all the needed methods
    def __init__(self, values=[]):
        # sets the default head pointer to None
        self.head_pointer = None
        # sets the default length of the list to zero 
        # and push the passed values
        self.length = 0
        self.pushed_values(values)

    # returns the counter
    def __len__(self):
        return self.length

    # makes the object iterable by returning an iterable list of values
    def __iter__(self):
        # initializes the list
        linked_list = []
        # starts defining the node in the head pointer
        node = self.head_pointer
        # if the pointer is different to None, goes on
        while node is not None:
            # appends the node's value
            linked_list.append(node.value())
            # sets the value of the node to object that points 
            # to the next node
            node = node.next()
        # returns an iterator of the list
        return iter(linked_list)

    # returns the object that has the head pointer
    # if the linked list is empty, raises an exception
    def head(self):
        if self.head_pointer is None:
            raise EmptyListException("The list is empty.")
        else:
            return self.head_pointer

    # calls the push() function depending if the 
    # given value is a list or an int
    def pushed_values(self, values):
        if values is not None:
            if isinstance(values, int):
                self.push(values)
            else:
                for val in values:
                    self.push(val)

    # creates a Node class object with the passed values
    # and updates the head pointer and length values
    def push(self, value):
        new_node = Node(value, self.head_pointer)
        self.head_pointer = new_node
        self.length += 1

    # pops the last added node
    def pop(self):
        # if the pointer is None (empty list) raises an exception
        if self.head_pointer is None:
            raise EmptyListException("The list is empty.")
        # sets the value of a node to the current head pointer
        node = self.head_pointer
        # sets the head pointer to the next node using the next function
        self.head_pointer = node.next()
        # adjust the length of the list
        self.length -= 1
        # returns the value of the popped node using the value function
        return node.value()

    # creates a list of the iter object and 
    # returns a reversed version of it
    def reversed(self):
        lst = list(self.__iter__())
        return reversed(lst)

# class that raises the empty list exception
class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
