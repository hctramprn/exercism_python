"""Functions which helps the locomotive engineer to keep track of the train."""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*wagons_num):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    wagons = list(wagons_num)
    
    return wagons


# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    wagons = []
    a, b, *wag = each_wagons_id
    locomotive, *w = wag
    wagons += [locomotive] + list(missing_wagons) + list(w) + [a, b]
    
    return wagons


# TODO: define the 'add_missing_stops()' function
def add_missing_stops(route, **arbitrary_stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    *stops, = arbitrary_stops.values()
    route.update({'stops': stops})
    
    return route


# TODO: define the 'extend_route_information()' function
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route.update(more_route_information)
    
    return route


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    reds, blues, oranges = wagons_rows
    depot = [list(group) for group in zip(reds, blues, oranges)]

    return depot
