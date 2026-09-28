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

def task3(edges):
    order = []
    vis = [0]*len(edges)
    q = queue.Queue()
    q.put(1)
    vis[1] = 1
    while not q.empty():
        p = q.get()
        order.append(p-1)
        for nxt in edges[p]:
            if vis[nxt] == 0:
                q.put(nxt)
                vis[nxt] = 1
    return order

# string = input()
# print(task3(to_zero_index(string)))
