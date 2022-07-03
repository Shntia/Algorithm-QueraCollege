n = int(input())
answer = 0
for a in range(n):
    for b in range(a, n - a):
        c = n - a - b
        if a + b > c >= b:
            answer = answer + 1

print(answer)
