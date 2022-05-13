def run():
    input_data = (
            ("Scrimshaw Whale's Tooth", '2A', 'Deserted Docks', ('2', 'A'), 'Blue'),
            ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
            ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
            ('Glass Starfish', '6D', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
            ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
            ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange'),
            ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
            ('Model Ship in Large Bottle', '8A', 'Harbor Managers Office', ('8', 'A'), 'Purple'),
            ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple'),
            ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple'),
            ('Amethyst  Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
            ('Antique Glass Fishnet Float', '3D', 'Spiky Rocks', ('3', 'D'), 'Yellow'),
            ('Silver Seahorse', '4E', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')
        )
    report = """"""
    for treasure in input_data:
        report += f'({treasure[0]}, {treasure[2]}, {treasure[3]}, {treasure[4]})\n'
    print(report)

if __name__ == '__main__':
    run()