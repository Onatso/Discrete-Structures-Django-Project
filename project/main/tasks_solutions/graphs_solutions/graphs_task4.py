import ast
import queue
def to_zero_index(string):
    g = []
    g.append([])
    t = ast.literal_eval(string)
    for el in t:
        for i in range(len(el)):
            el[i] += 1
        g.append(el)
    return g

def task4(edges, order):
    depth = [0]*len(edges)
    depth[order[0]] = 1
    q = queue.Queue()
    q.put(order[0])
    mx = 0
    while not q.empty():
        p = q.get()
        for nxt in edges[p]:
            if depth[nxt] == 0:
                depth[nxt] = depth[p] + 1
                q.put(nxt)
                mx = max(mx, depth[nxt])
    cnt1 = [0]*(mx+1)
    cnt2 = [0]*(mx+1)
    vis = [0]*len(edges)
    q.put(order[0])
    vis[order[0]] = 1
    c = 0
    while not q.empty():
        p = q.get()
        cnt1[depth[p]] += 1
        cnt2[depth[order[c]]] += 1
        if cnt2[depth[order[c]]] > cnt1[depth[order[c]]]:
            return False
        for nxt in edges[p]:
            if vis[nxt] == 0:
                q.put(nxt)
                vis[nxt] = 1
        c += 1
    return True

#string1 = input()
#string2 = input()
# print(task4(to_zero_index(string1), list(map(int, string2.split()))))
