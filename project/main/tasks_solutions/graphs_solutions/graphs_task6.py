import ast
def to_zero_index(string):
    g = []
    g.append([])
    t = ast.literal_eval(string)
    for el in t:
        for i in range(len(el)):
            el[i] += 1
        g.append(el)
    return g

def dfs(pos, g, vis):
    vis[pos] = 1
    for nxt in g[pos]:
        if vis[nxt] == 0:
            dfs(nxt, g, vis)

def task56(edges):
    cnt = 0
    vis = [0]*len(edges)
    for i in range(1, len(edges)):
        if vis[i] == 0:
            cnt += 1
            dfs(i, edges, vis)
    return cnt

# string = input()
# print(task56(to_zero_index(string)))
