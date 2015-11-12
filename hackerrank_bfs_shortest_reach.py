import sys

def run(S):
    nodes = [idx+1 for idx, x in enumerate(eds[S-1]) if x==1]
    n = None
    for n in nodes:
        existing = SD[n-1]
        if existing != sys.maxint:
            SD[n-1] = min(SD[S-1] + 1, SD[n-1])
        else:
            SD[n-1] = SD[S-1] + 1
    print S, SD
    for n in nodes:
        run(n)

f = open("input02.txt")
T = int(f.readline())
for test in range(T):
    N, M = map(int, f.readline().split(' '))
    eds = []
    for i in range(N): eds.append([0]*N)
    for i in range(M):
        n1,n2 = map(int, f.readline().split(' '))
        eds[n1-1][n2-1] = 1
    S = int(f.readline())
    for l in eds: print l
    print S
    SD = [sys.maxint] * N
    SD[S-1] = 0
    run(S)
