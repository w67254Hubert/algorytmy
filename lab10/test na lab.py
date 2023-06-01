
def bfs(g,s):

    n=len(g)
    visited=[False]*n
    d=[-1]*n
    p=[-1]*n


    visited[s]=True
    d[s] = 0
    Q=Queue()
    Q.put(s):

    while not Q.empty():
        u=Q.get()

        for v in range(n):
            if g[u][v]==1 and visited[v]:
                visited[v]=True
                d[v]=d[u]+1
                p[v]=u
                q.put(v)

    return visited, d, p

g=[
    [0,1,1,0,0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0]
]

for v in range(len(g)):
    print("wieszchołąek"{v}"visited)"