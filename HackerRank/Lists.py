if __name__ == '__main__':
    N = int(input())
    result_list = []

    # Very inefficient approach.
    for i in range(0, N):
        rawCommand = list(input().split())
        command = rawCommand[0]
        if command == 'insert':
            i = int(rawCommand[1])
            e = int(rawCommand[2])
            result_list.insert(i, e)
        elif command == 'print':
            print(result_list)
        elif command == 'remove':
            e = int(rawCommand[1])
            result_list.remove(e)
        elif command == 'append':
            e = int(rawCommand[1])
            result_list.append(e)
        elif command == 'sort':
            result_list.sort()
        elif command == 'pop':
            result_list.pop()
        elif command == 'reverse':
            result_list.reverse()
        else:
            print("Invalid command")



