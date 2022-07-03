line_one = input().split()
line_two = input().split()

c = [i for i in line_two]
d = [input() for i in range(int(line_one[1]))]

sad = list(map(lambda x: sum(map(lambda y: 1 if y < x else 0, c)), d))

print(*sad, sep="\n")
