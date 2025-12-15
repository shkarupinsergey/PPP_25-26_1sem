

if __name__ == "__main__":
    pass # Ваш код здесь
def poisk_ciklov(adj):
    n = len(adj)
    cikly = []
    sost = []

    def dfs(v, pos, marsh):
        sost.append((v, pos.copy(), marsh.copy(), cikly.copy()))

        pos[v] = 1
        marsh.append(v)

        for u in range(n):
            if adj[v][u] == 1:
                if u in marsh:
                    i = marsh.index(u)
                    cikl = marsh[i:] + [u]
                    if cikl not in cikly:
                        cikly.append(cikl)
                elif pos[u] == 0:
                    dfs(u, pos, marsh)

        marsh.pop()
        pos[v] = 0

    for i in range(n):
        pos = [0] * n
        marsh = []
        dfs(i, pos, marsh)

    return cikly, sost

adj = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

cikly, sost = poisk_ciklov(adj)

print("Найденные циклы:")
for c in cikly:
    print(c)

print("Состояния обхода (первые 5):")
for s in sost[:5]:
    print(s)
