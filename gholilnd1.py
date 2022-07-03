line_one = input().split()
population = int(line_one[0])
days = int(line_one[1])
c = []
d = []
sads = {}

if 1 <= population <= 1000 and 1 <= days <= 1000:
    line_two = input().split()
    count = 0
    for i in line_two:
        if 1 <= int(i) <= 1000000:
            c.append(i)
            count += 1
    for i in range(days):
        line_three = input().split()
        for j in line_three:
            if 1 <= int(j) <= 1000000:
                d.append(j)

    for i in range(days):
        sads[i] = 0
        for t in c:
            if d[i][0] > t:
                sads[i] += 1
    for day in sads:
        print(sads[day])

