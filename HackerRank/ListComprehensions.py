if __name__ == '__main__':
    # Following is repetitive.
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    # This sort of seems better? It's an option.
    # TODO find out what this is. I think it's called a 'generator expression'
    x, y, z, n = (int(input()) for _ in range(4))

    result = [
                [i, j, k]
                for i in range(x + 1)
                for j in range(y + 1)
                for k in range(z + 1)
                if i + j + k != n
             ]

    print(result)
