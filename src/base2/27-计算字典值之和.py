def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
    return sum


if __name__ == '__main__':
    dict = {'a': 100, 'b': 200, 'c': 300}
    print("Sum :", returnSum(dict))
