""" Created by Jieyi on 7/28/16. """
import sys
from copy import deepcopy


def dijkstra(path_map, start=0):
    arr_shortest_path = path_map[start]
    stack = []

    # Until all vertices put into stack.
    while 1:
        if len(stack) is len(arr_shortest_path):
            break

        # Pick the smallest value from the arr_shortest_path is not including vertices in the stack.
        tmp_arr = arr_shortest_path[:]
        for i in range(len(stack)):
            tmp_arr[stack[i]] = sys.maxsize
        mini_vertex = arr_shortest_path.index(min(tmp_arr))
        stack.append(mini_vertex)

        # Calculate the smallest value's vertex with all vertices which it could go.
        for i in range(len(arr_shortest_path)):
            if arr_shortest_path[i] > arr_shortest_path[mini_vertex] + path_map[mini_vertex][i]:
                arr_shortest_path[i] = arr_shortest_path[mini_vertex] + path_map[mini_vertex][i]

    return arr_shortest_path


def algorithm():
    while True:
        n, s = map(int, input().split(' '))
        if n == 0 and s == 0:
            break

        # Create two maps.
        g_money = [[sys.maxsize for _ in range(s)] for _ in range(s)]
        for c in range(s):
            g_money[c][c] = 0
        g_time = deepcopy(g_money)

        # Set two maps.
        for _ in range(n):
            x, y, money, time = map(int, input().split(' '))
            x, y = x - 1, y - 1
            g_money[x][y], g_time = money, time

        # Calculate the shortest path.
        for n in range(int(input())):
            start, end, category = list(map(int, input().split(' ')))
            m = {0: g_money, 1: g_time}.get(category)
            ans = dijkstra(m, start - 1)
            print(ans[end - 1])


def main():
    algorithm()


if __name__ == '__main__':
    main()
