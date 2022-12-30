def largest_product(series, size):
    # raises ValueErrors if the series or size are not adecuate
    if len(series) < size:
        raise ValueError('span must be smaller than string length')
    if size < 0:
        raise ValueError('span must not be negative')
    if size == 0:
        return 1
    else:
        try:
            int(series)
        except:
            raise ValueError('digits input must only contain digits')

    # loop that creates all the possible subseries
    subseries = []
    for i in range(len(series) - size + 1):
        subseries.append(list(series[i:i + size]))

    # loop that gets the product of all the subseries
    products = []
    for sublist in subseries:
        prod = 1
        for num in sublist:
            prod = prod * int(num)
        products.append(prod)

    # returns the first number of the sorted products list
    return (sorted(products, reverse=True))[0]
