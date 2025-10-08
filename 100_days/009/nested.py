travel = {
    "France": ['Paris', 'Lille', 'Ginon'],
    "Germany": ['A', 'B', 'C'],
}

print(travel['France'][1])

nested_list = ['A','B',['C','D']]
print(nested_list[2][0])

travel_2 = {
    "France": {
        "num_vis": 6,
        "cities": ['Paris', 'Lille', 'Ginon'],
    },
    "Germany": ['A', 'B', 'C'],
}

print(travel_2['France']['cities'][0])