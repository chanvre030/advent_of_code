import numpy as np

data = open("input_day12.txt", "r").read().split("\n")
connections = {}
for d in data:
    d = d.split("-")
    for i in range(len(d)):
        if d[i - 1] != 'start':
            if d[i] in connections:
                connections[d[i]].append(d[i-1])
            else:
                connections[d[i]] = [d[i - 1]]

routes = [['start']]
final_routes = []
while len(routes) > 0:
    new_routes = []
    for route in routes:
        for dest in connections[route[-1]]:
            skip = False
            if dest.islower() and dest in route:
                unique, counts = np.unique(np.array(route), return_counts=True)
                for point in route:
                    if point.islower():
                        if counts[np.where(unique == point)][0] > 1:
                            skip = True
            if not skip:
                new_route = route.copy()
                new_route.append(dest)
                if dest != 'end':
                    new_routes.append(new_route)
                else:
                    final_routes.append(new_route)
    routes = new_routes
    print(len(final_routes))
print("number of routes:", len(final_routes))
