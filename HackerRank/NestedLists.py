if __name__ == '__main__':
    scoreList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scoreList.append([score, name])

    scoreList = sorted(scoreList)

    lowestScore = scoreList[0][0]
    foundSecondLowest = False
    secondLowestNames = []
    for i in range(1, len(scoreList)):
        currentScore = scoreList[i][0]
        if not foundSecondLowest:
            if currentScore > lowestScore:
                foundSecondLowest = True;
                secondLowestScore = currentScore;
                secondLowestNames.append(scoreList[i][1])
        else:
            if secondLowestScore == currentScore:
                secondLowestNames.append(scoreList[i][1])
            else:
                break;

    secondLowestNames = sorted(secondLowestNames)
    for name in secondLowestNames:
        print(name)
