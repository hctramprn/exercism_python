NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        # Initialize empty lists and a dictionary
        self.nodes = []
        self.edges = []
        self.attrs = {}
        # Call the get_graph method to populate the graph based on the data input
        self.get_graph(data)

    def get_graph(self, data):
        # If data is a list of instructions
        if isinstance(data, list):
            # Check that the first item in the first instruction is present
            if len(data[0]) < 3:
                # If not, raise a TypeError indicating that the item is incomplete
                raise TypeError('Graph item incomplete')
            # Iterate over the instructions
            for instructions in data:
                # Get the task code from the first item in the instruction
                task = instructions[0]
                # Based on the task code, add a node, edge, or attribute to the graph
                if task == 0:
                    # Check that the node name is a string and add the node to the graph
                    if not isinstance(instructions[1], str):
                        raise ValueError('Node is malformed')
                    self.nodes.append(Node(instructions[1], instructions[2]))
                elif task == 1:
                    # Check that the edge name is a string and add the edge to the graph
                    if not isinstance(instructions[1], str):
                        raise ValueError('Edge is malformed')
                    self.edges.append(
                        Edge(instructions[1], instructions[2], instructions[3]))
                elif task == 2:
                    # Check that the attribute name is a string and add the attribute to the graph
                    if not isinstance(instructions[1], str):
                        raise ValueError('Attribute is malformed')
                    self.attrs.update({instructions[1]: instructions[2]})
                else:
                    # If the task code is not recognized, raise a ValueError indicating an unknown item
                    raise ValueError('Unknown item')
        # If data is not a list, raise a TypeError indicating that the data is malformed
        elif isinstance(data, int) or isinstance(data, str):
            raise TypeError('Graph data malformed')
        # Return nothing
        return
