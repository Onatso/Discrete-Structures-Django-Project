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

def task2(edges, order):
    stack = []
    vis = [0]*(len(edges))
    vis[order[0]] = 1
    stack.append(order[0])
    p = 1
    while len(stack) > 0 and p < len(order):
        if order[p] in edges[stack[-1]]:
            vis[order[p]] += 1
            stack.append(order[p])
            p += 1
        else:
            stack.pop()
    for i in range(1, len(edges)):
        if vis[i] != 1:
            return False
    return True

# string1 = input()
# string2 = input()
# print(task2(to_zero_index(string1), list(map(int, string2.split()))))
