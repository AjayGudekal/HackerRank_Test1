# HackerRank Program to print minimum difference between elements in array
# This takes number of elements as input in first line & from second line each element should be given as input
def closestNumbers(numbers):
    d = []
    pos = 0
    for i in numbers:
        pos += 1

        for j in range(pos, len(numbers)):
            v = []
            k = i - numbers[j]
            v.append(abs(k))
            v.append(i)
            v.append(numbers[j])
            d.append(v)
    d.sort()
    c = d[0][0]
    # print(d)
    for i in d:
        res=[]
        if i[0] == c:
            res.append(i[1])
            res.append(i[2])
            res.sort()
            print(str(res[0]) + ' ' + str(res[1]))
if __name__ == '__main__':
    numbers_count = int(input())
    numbers = []
    for _ in range(numbers_count):
        numbers_item = int(input())
        numbers.append(numbers_item)
    closestNumbers(numbers)
