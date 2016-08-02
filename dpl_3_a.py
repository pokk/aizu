""" Created by Jieyi on 7/16/16. """


def algorithm():
    r, c = map(int, input().split(' '))

    ans_matrix = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
    input_matrix = []

    for _ in range(r):
        input_matrix.append(list(map(int, input().split(' '))))

    largest_square = 0

    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])):
            new_i, new_j = i + 1, j + 1
            if input_matrix[i][j] == 0:
                ans_matrix[new_i][new_j] = min(ans_matrix[new_i - 1][new_j], ans_matrix[new_i][new_j - 1], ans_matrix[new_i - 1][new_j - 1]) + 1
                largest_square = ans_matrix[new_i][new_j] if ans_matrix[new_i][new_j] > largest_square else largest_square
            else:
                ans_matrix[new_i][new_j] = 0

    print(largest_square ** 2)


def main():
    algorithm()


if __name__ == '__main__':
    main()
