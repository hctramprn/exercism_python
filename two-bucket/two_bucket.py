def measure(bucket_one, bucket_two, goal, start_bucket):
    # Check if the goal is achievable based on the GCD of the bucket capacities and the goal
    has_solution = gcd(bucket_one, bucket_two, goal)
    if not has_solution or goal > max(bucket_one, bucket_two):
        raise ValueError('There is no solution.')

    # Set the initial state based on the start bucket
    if start_bucket == 'one':
        b1 = bucket_one
        b2 = 0
        forbidden_combination = (0, bucket_two)
    else:
        b1 = 0
        b2 = bucket_two
        forbidden_combination = (bucket_one, 0)

    # Initialize a list of actions with the initial state
    actions = [[(b1, b2)]]
    liters_in_buckets = {b1, b2}

    # Perform breadth-first search to find the optimal solution
    while goal not in liters_in_buckets:
        temp_actions = list()
        for action in actions:
            last_b1, last_b2 = action[-1]

            # Fill the first bucket to its capacity if it's not already full
            filled = fill_bucket(last_b1, bucket_one, last_b2, False)
            if filled not in action and filled != forbidden_combination:
                temp_actions.append(action + [filled])
                liters_in_buckets.update(filled)

            # Empty the first bucket if it's not already empty
            emptied = empty_bucket(last_b1, last_b2, False)
            if emptied not in action and emptied != forbidden_combination:
                temp_actions.append(action + [emptied])
                liters_in_buckets.update(emptied)

            # Pour water from the first bucket to the second bucket
            poured = pour_bucket(last_b1, last_b2, bucket_two, False)
            if poured not in action and poured != forbidden_combination:
                temp_actions.append(action + [poured])
                liters_in_buckets.update(poured)

            # Fill the second bucket to its capacity if it's not already full (reverse pouring)
            filled_rev = fill_bucket(last_b2, bucket_two, last_b1, True)
            if filled_rev not in action and filled_rev != forbidden_combination:
                temp_actions.append(action + [filled_rev])
                liters_in_buckets.update(filled_rev)

            # Empty the second bucket if it's not already empty (reverse pouring)
            emptied_rev = empty_bucket(last_b2, last_b1, True)
            if emptied_rev not in action and emptied_rev != forbidden_combination:
                temp_actions.append(action + [emptied_rev])
                liters_in_buckets.update(emptied_rev)

            # Pour water from the second bucket to the first bucket (reverse pouring)
            poured_rev = pour_bucket(last_b2, last_b1, bucket_one, True)
            if poured_rev not in action and poured_rev != forbidden_combination:
                temp_actions.append(action + [poured_rev])
                liters_in_buckets.update(poured_rev)

        actions = temp_actions

    # Find the action sequence that leads to the goal and return the result
    for act in actions:
        if goal in act[-1]:
            total_actions = len(act)
            first, second = act[-1]
            if first == goal:
                return (total_actions, 'one', second)
            return (total_actions, 'two', first)


def gcd(a, b, goal):
    # Calculate the greatest common divisor (GCD) using the Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    # Check if the goal is divisible by the GCD
    return goal % a == 0


def fill_bucket(first, first_cap, second, reverse):
    # Fill a bucket to its capacity
    if first < first_cap:
        first = first_cap
    if not reverse:
        return (first, second)
    return (second, first)


def empty_bucket(first, second, reverse):
    # Empty a bucket
    if first:
        first = 0
    if not reverse:
        return (first, second)
    return (second, first)


def pour_bucket(first, second, second_cap, reverse):
    # Pour water from one bucket to another
    if first > 0 and second < second_cap:
        if second + first <= second_cap:
            second = second + first
            first = 0
        elif second + first > second_cap:
            first = first - (second_cap - second)
            second = second_cap

    if not reverse:
        return (first, second)
    return (second, first)
