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

def dfs(pos, g, vis, order):
    vis[pos] = 1
    order.append(pos)
    for nxt in g[pos]:
        if vis[nxt] == 0:
            dfs(nxt, g, vis, order)

def task1(edges):
    order = []
    vis = [0]*len(edges)
    dfs(1, edges, vis, order)
    return order

