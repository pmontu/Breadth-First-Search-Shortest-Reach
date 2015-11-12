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
    #run(N, eds, S)

def run(N, eds, S):
    bfs_ar = [[S]]
    weight = 6
    def calc(bfs_ar):
        new_bfs_ar = []
        isChanged = False
        for bfs in bfs_ar:
            search_node = bfs[-1]
            n = set([ed[1] for ed in eds if ed[0]==search_node])
            i = _not_assigned = object()
            for i in n:
                new_bfs_ar.append(bfs + [i])
                isChanged = True
            if i is _not_assigned:
                new_bfs_ar.append(bfs)
        if isChanged:
            bfs_ar = new_bfs_ar
            return bfs_ar
        else: return None

    while True:
        t = calc(bfs_ar)
        if not t:
            break
        bfs_ar = t

    import sys
    pos = [sys.maxint] * N
    for bfs in bfs_ar:
        for idx, n in enumerate(bfs):
            pos[n-1] = min(pos[n-1], idx*weight)
    pos = [str(x) if x != sys.maxint else "-1" for x in pos]
    del pos[S-1]
    print " ".join(pos)