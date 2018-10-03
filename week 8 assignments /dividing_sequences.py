def best(i):
    StoredBest[0] = 1
    for i in range(n):
        m = 1
        for j in range(i):
            if a[i] % a[j] == 0:
                m = max(m,(StoredBest[j] + 1))

        StoredBest[i] = m



n = int(input())
a = []
StoredBest = [0]*n
for i in range(n):
    a.append(int(input()))
l = best(0)


print(max(StoredBest))


