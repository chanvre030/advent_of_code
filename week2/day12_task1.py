import os

from pathlib import Path


def main():
    parent = Path(__file__).parent.resolve()
    txt = "input_day12.txt"
    path = os.path.join(parent, txt)
    data = open(path, "r").read().split("\n")
    connections = {}
    for d in data:
        d = d.split("-")
        for i in range(len(d)):
            if d[i - 1] != 'start':
                if d[i] in connections:
                    connections[d[i]].append(d[i - 1])
                else:
                    connections[d[i]] = [d[i - 1]]
    routes = [['start']]
    final_routes = []
    while len(routes) > 0:
        new_routes = []
        for route in routes:
            for dest in connections[route[-1]]:
                if dest.islower() and dest in route:
                    continue
                new_route = route.copy()
                new_route.append(dest)
                if dest != 'end':
                    new_routes.append(new_route)
                else:
                    final_routes.append(new_route)
        routes = new_routes
    print("number of routes:", len(final_routes))


if __name__ == "__main__":
    main()

