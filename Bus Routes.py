class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)

        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus)

        q = deque()
        visited_buses = set()
        visited_stops = {source}

        q.append((source, 0))

        while q:
            stop, buses_taken = q.popleft()

            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue

                visited_buses.add(bus)

                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses_taken + 1

                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append((next_stop, buses_taken + 1))

        return -1
