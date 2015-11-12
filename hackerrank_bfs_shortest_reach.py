import sys

def fwd(S):
    nodes = [idx+1 for idx, x in enumerate(eds[S-1]) if x==1]
    n = None
    for n in nodes:
        existing = SD[n-1]
        if existing != sys.maxint:
            SD[n-1] = min(SD[S-1] + 1, SD[n-1])
        else:
            SD[n-1] = SD[S-1] + 1
    for n in nodes:
        fwd(n)

def rev(S):
    nodes = []
    for idx, l in enumerate(eds):
        if l[S-1] == 1:
            nodes.append(idx+1)
    for n in nodes:
        existing = SD[n-1]
        if existing != sys.maxint:
            SD[n-1] = min(SD[S-1] + 1, SD[n-1])
        else:
            SD[n-1] = SD[S-1] + 1
    for n in nodes:
        rev(n)


f = open("input01.txt")
T = int(f.readline())
for test in range(T):
    N, M = map(int, f.readline().split(' '))
    eds = []
    for i in range(N): eds.append([0]*N)
    for i in range(M):
        n1,n2 = map(int, f.readline().split(' '))
        eds[n1-1][n2-1] = 1
    S = int(f.readline())
    SD = [sys.maxint] * N
    SD[S-1] = 0
    fwd(S)
    rev(S)
    del SD[S-1]
    SD = [str(sd*6) if sd!=sys.maxint else "-1" for sd in SD]
    print " ".join(SD)
