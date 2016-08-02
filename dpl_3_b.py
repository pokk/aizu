""" Created by Jieyi on 7/25/16. """


# This fail the judgement.

def max_rectangle(array):
    max_area = 0

    for i in range(1, max(array) + 1):
        current_area = 0
        for j in range(len(array)):
            if array[j] >= i:
                current_area += i
                if current_area > max_area:
                    max_area = current_area
            else:
                current_area = 0

    return max_area


def new_max_rectangle(array):
    max_area = 0

    for i in range(len(array)):
        min_height = array[i]
        width = 1
        for j in range(i, len(array)):
            if array[j] == 0:
                width = 1
                if j < i:
                    min_height = array[j + 1]
                continue
            min_height = array[j] if min_height > array[j] else min_height
            max_area = width * min_height if width * min_height > max_area else max_area
            width += 1

    return max_area


def algorithm():
    r, c = map(int, input().split(' '))

    ans_array = [0 for _ in range(c)]
    input_matrix = []

    for _ in range(r):
        input_matrix.append(list(map(int, input().split(' '))))

    largest_square = 0

    for i in range(r):
        for j in range(c):
            ans_array[j] = ans_array[j] + 1 if input_matrix[i][j] == 0 else 0
        m = new_max_rectangle(ans_array)
        largest_square = largest_square if largest_square > m else m

    print(largest_square)


def main():
    algorithm()


if __name__ == '__main__':
    main()
