""" Created by Jieyi on 7/28/16. """
from collections import defaultdict
import io
import sys
import heapq

if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)


def dijkstra(graph, start, end, total_vertices):
    h = []
    shortest_path = [0 if i == start else sys.maxsize for i in range(total_vertices + 1)]
    heapq.heappush(h, (start, 0))

    while True:
        vertex, value = heapq.heappop(h)
        if end == vertex:
            break

        for k, v in graph.get(vertex):
            if shortest_path[k] > value + v:
                shortest_path[k] = value + v
                heapq.heappush(h, (k, shortest_path[k]))

    return shortest_path


def algorithm():
    while True:
        n, s = map(int, input().split())
        if n == 0 and s == 0:
            break

        # Create two maps.
        g_money = defaultdict(list)
        g_time = defaultdict(list)

        # Set two maps.
        for _ in range(n):
            start, end, money, time = map(int, input().split())
            g_money[start].append((end, money))
            g_money[end].append((start, money))
            g_time[start].append((end, time))
            g_time[end].append((start, time))

        # Calculate the shortest path.
        for n in range(int(input())):
            start, end, category = list(map(int, input().split()))
            m = {0: g_money, 1: g_time}.get(category)
            ans = dijkstra(m, start, end, s)
            print(ans[end])


def main():
    algorithm()


if __name__ == '__main__':
    main()
