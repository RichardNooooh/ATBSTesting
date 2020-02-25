if __name__ == '__main__':
    n = int(input())
    result = {}
    for _ in range(n):
        name, *marks = input().split()
        scores = map(float, marks)
        avg = sum(scores) / 3
        result[name] = avg

    print(f'{result.get(input()):.2f}')
