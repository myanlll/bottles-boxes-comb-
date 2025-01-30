def combination(capacity, bottles):
    if bottles < 1:
        return set()

    combinations = [[i] for i in range(capacity + 1)]

    for i in range(1, bottles):
        new_combinations = []
        for combo in combinations:
            total_capacity = capacity - sum(combo)
            for i in range(total_capacity + 1):
                new_combinations.append(combo + [i])
        combinations = new_combinations

    combinations = [combo for combo in combinations if sum(combo) > 0]
    
    valid_combinations = [tuple(combo) for combo in combinations if sum(combo) <= capacity]

    return set(valid_combinations)

bottles = int(input("Enter the number of bottle types: "))
capacity = int(input("Enter the box capacity: "))

valid_combinations = combination(capacity, bottles)
print(f"A total of {len(valid_combinations)} different combinations were found.")
for combo in valid_combinations:
    print(combo)
print(f"A total of {len(valid_combinations)} different combinations were found.")
