import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pow
from itertools import permutations


def calculate_distance(point_1, point_2):
    return sqrt(pow(point_2[0] - point_1[0], 2) + pow(point_2[1] - point_1[1], 2))


def get_all_routes(start_city, cities):
    all_routes = []
    for route in permutations(cities):
        all_routes.append([start_city] + list(route))

    return all_routes


def brute_force(cities):
    all_routes = get_all_routes(cities[0], cities[1:])
    shortest_distance = 1000
    shortest_route = []

    for route in all_routes:
        route_distance = 0
        for i in range(0, len(route)):
            first = route[i]
            second = route[i + 1] if i != len(route) - 1 else route[0]

            route_distance = route_distance + calculate_distance(first, second)

        if route_distance < shortest_distance:
            shortest_distance = route_distance
            shortest_route = route

    print("Brute force method total distance: %f\n" % shortest_distance)
    return shortest_route


def nearest_neighbor(cities):
    visited = [cities[0]]
    total_distance = 0
    current_lowest_distance = [[0, 0], 1000]

    while len(visited) != len(cities):
        for city in cities[1:]:
            if city not in visited:
                distance = calculate_distance(visited[-1], city)
                if distance < current_lowest_distance[1]:
                    current_lowest_distance = [city, distance]

        visited.append(current_lowest_distance[0])
        total_distance = total_distance + current_lowest_distance[1]
        current_lowest_distance = [[0, 0], 1000]

    total_distance = total_distance + calculate_distance(visited[0], visited[-1])
    print("Nearest neighbor method total distance: %f\n" % total_distance)
    return visited


def draw_route(route, color):
    for i in range(0, len(route)):
        first = route[i]
        second = route[i + 1] if i != len(route) - 1 else route[0]
        label_shift = 0.004

        plt.plot(
            [first[0], second[0]],
            [first[1], second[1]],
            color=color,
            linestyle="dashed",
        )
        plt.text(
            first[0] + label_shift, first[1] + label_shift, "%d" % (i + 1), fontsize=12
        )


print("Type in number of cities: ")
N = int(input())
x = np.random.rand(N)
y = np.random.rand(N)
cities = []

for i in range(0, N):
    cities.append([x[i], y[i]])

# Nearest neighbor
route = nearest_neighbor(cities)
draw_route(route, "red")
plt.scatter(x, y)
plt.show()

# Brute force
route = brute_force(cities)
draw_route(route, "green")
plt.scatter(x, y)
plt.show()
