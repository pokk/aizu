""" Created by Jieyi on 10/31/16. """
import heapq
import io
import sys
from collections import defaultdict

if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)


def input_data():
    while True:
        tickets, vertices, edges, start, end = map(int, input().split())
        if 0 == tickets + vertices + edges + start + end:
            break

        shortest_path = [[sys.maxsize for _ in range(vertices + 1)] for _ in range(tickets + 1)]
        for i in range(tickets + 1):
            shortest_path[i][start] = 0
        g = defaultdict(list)
        h = []
        # Generate a map.
        for _ in range(edges):
            i, j, fare = map(int, input().split())
            g[i].append((j, fare))
            g[j].append((i, fare))
        # (price, vertices, remainder ticket)
        heapq.heappush(h, (0, start, tickets))

        while True:
            if 0 == len(h):
                break
            ori_price, vertex, remain_ticket = heapq.heappop(h)
            for v, price in g[vertex]:
                if shortest_path[remain_ticket][v] > ori_price + price:
                    shortest_path[remain_ticket][v] = min(shortest_path[remain_ticket][v], ori_price + price)
                    heapq.heappush(h, (shortest_path[remain_ticket][v], v, remain_ticket))
                if remain_ticket and shortest_path[remain_ticket - 1][v] > ori_price + int(price / 2):
                    shortest_path[remain_ticket - 1][v] = min(shortest_path[remain_ticket - 1][v], ori_price + int(price / 2))
                    heapq.heappush(h, (shortest_path[remain_ticket - 1][v], v, remain_ticket - 1))

        cheapest = sys.maxsize
        for i in range(tickets):
            cheapest = min(shortest_path[i][end], cheapest)
        print(cheapest)


def main():
    input_data()


if __name__ == '__main__':
    main()
