f = open("input01.txt")
T = int(f.readline())
for test in range(T):
    N, M = map(int, f.readline().split(' '))
    eds = {}
    for i in range(M):
        n1,n2 = map(int, f.readline().split(' '))
        if n1 in eds:
            if n2 not in eds[n1]:
                eds[n1].append(n2)
        else:
            eds[n1] = [n2]
        if n2 in eds:
            if n1 not in eds[n2]:
                eds[n2].append(n1)
        else:
            eds[n2] = [n1]
    S = int(f.readline())

    visited = [False] * N
    queue = []
    queue.append(S)
    visited[S-1] = True
    level = 0

    import sys
    distance = [sys.maxint] * N
    distance[S-1] = 0

    while(queue):
        s = queue.pop(0)
        if s in eds:
            for t in eds[s]:
                if not visited[t-1]:
                    visited[t-1] = True
                    queue.append(t)
                    distance[t-1] = distance[t-1] + distance[s-1] + 1 if distance[t-1] != sys.maxint else distance[s-1] + 1

    del distance[S-1]
    distance = [str(x*6) if x!=sys.maxint else "-1" for x in distance]
    print " ".join(distance)