"""Problem 787. Cheapest Flights Within K Stops

Constraints:
    There will not be any multiple flights between two cities.
    1 <= n <= 100
    0 <= flights.length <= (n * (n - 1) / 2)
    flights[i].length == 3
    0 <= fromi, toi < n
    fromi != toi
    1 <= pricei <= 10^4
    0 <= src, dst, k < n
    src != dst

Algorithm
    Uses a BFS approach that accounts for multiple visits to each node.
    As long as we meet the requirement on number of stops and a higher
    number of stops results in a lower tatal price.
"""

from typing import List, Dict, Tuple
from collections import deque, namedtuple


def find_cheapest_price(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    graph = _model_as_graph(n, flights)
    city_queue = deque()
    min_price_paths = {}
    StopsPrice = namedtuple("StopsPrice", "stops, price")
    CityStopsPrice = namedtuple("CityStopsPrice", "city, stops, price")
    city_queue.appendleft(CityStopsPrice(city=src, stops=-1, price=0))
    min_price_paths[src] = [StopsPrice(stops=-1, price=0)]
    while city_queue:
        current = city_queue.pop()
        if current.stops < k:
            for neighbor, price in graph[current.city]:
                should_append = False
                if neighbor not in min_price_paths:
                    min_price_paths[neighbor] = [
                        StopsPrice(stops=current.stops + 1, price=current.price + price)
                    ]
                    should_append = True
                else:
                    last = min_price_paths[neighbor][-1]
                    if current.price + price < last.price:
                        if last.stops == current.stops + 1:
                            min_price_paths[neighbor].pop()
                        min_price_paths[neighbor].append(
                            StopsPrice(
                                stops=current.stops + 1, price=current.price + price
                            )
                        )
                        should_append = True
                if should_append:
                    city_queue.appendleft(
                        CityStopsPrice(
                            city=neighbor,
                            stops=min_price_paths[neighbor][-1].stops,
                            price=min_price_paths[neighbor][-1].price,
                        )
                    )
    if dst not in min_price_paths:
        return -1
    return min_price_paths[dst][-1].price


def _model_as_graph(
    n: int, flights: List[List[int]]
) -> Dict[int, List[Tuple[int, int]]]:
    graph = dict([(i, []) for i in range(n)])
    for src_city, dest_city, price in flights:
        graph[src_city].append((dest_city, price))
    return graph
