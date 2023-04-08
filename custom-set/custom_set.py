class CustomSet:
    def __init__(self, elements=[]):
        """
        Initialize a CustomSet object with an optional list of elements.
        The elements are sorted and stored in self.elements.
        The sorted elements are also joined into a string and stored in self.elements_str.
        """
        self.elements = sorted(elements)
        self.elements_str = ''.join([str(el) for el in self.elements])

    def isempty(self):
        """
        Return True if the set is empty, False otherwise.
        """
        if not self.elements:
            return True
        return False

    def __contains__(self, element):
        """
        Check if an element is present in the set.
        Return True if the element is present, False otherwise.
        """
        if element in self.elements:
            return True
        return False

    def issubset(self, other):
        """
        Check if the current set is a subset of another set.
        Return True if self is a subset of other, False otherwise.
        """
        if self.elements_str in other.elements_str:
            return True
        return False

    def isdisjoint(self, other):
        """
        Check if the current set is disjoint (has no elements in common) with another set.
        Return True if the sets are disjoint, False otherwise.
        """
        if len(self.elements) == 0 and len(other.elements) == 0:
            # Both sets are empty
            return True

        for el in self.elements:
            if el in other.elements:
                # There is at least one common element
                return False
        # No common elements found
        return True

    def __eq__(self, other):
        """
        Check if two sets are equal.
        Return True if the sets have the same elements, False otherwise.
        """
        if self.elements == other.elements:
            return True
        return False

    def add(self, element):
        """
        Add an element to the set if it is not already present.
        """
        temp_lst = self.elements
        if element not in temp_lst:
            temp_lst.append(element)
        self.elements = sorted(temp_lst)

    def intersection(self, other):
        """
        Return a new set containing the elements that are common to the current set and another set.
        """
        set_lst = []
        for el in self.elements:
            if el in other.elements:
                set_lst.append(el)
        if not set_lst:
            # No common elements found
            return CustomSet()
        return CustomSet(set_lst)

    def __sub__(self, other):
        """
        Return a new set containing the elements that are in the current set but not in another set.
        """
        sub_lst = []
        for el in self.elements:
            if el not in other.elements:
                sub_lst.append(el)
        if not sub_lst:
            # No elements found in the current set that are not in the other set
            return CustomSet()
        return CustomSet(sub_lst)

    def __add__(self, other):
        """
        Return a new set containing the union of the current set and another set.
        """
        union_lst = []
        for cust_set in [self, other]:
            for el in cust_set.elements:
                if el not in union_lst:
                    union_lst.append(el)
        if not union_lst:
            # Both sets are empty
            return CustomSet()
        return CustomSet(union_lst)
