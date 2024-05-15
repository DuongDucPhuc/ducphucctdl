from collections import deque

def LienThong(dt):
    so_thanh_phan = 0
    danh_dau = [False] * len(dt)
    
    def DFS(u):
        danh_dau[u] = True
        
        for v in dt[u]:
            if not danh_dau[v]:
                DFS(v)
    for u in range(len(dt)):
        if not danh_dau[u]:
            so_thanh_phan += 1
            DFS(u)
    
    return so_thanh_phan == 1
dt1 = {0: [1, 3], 1: [0, 2, 3], 2: [1, 3], 3: [0, 1, 2]}
print(LienThong(dt1)) 


dt2 = {0: [1], 1: [0], 2: [3], 3: [2]}
print(LienThong(dt2))  


dt3 = {0: [1, 3], 1: [2], 2: [3], 3: []}
print(LienThong(dt3))  


dt4 = {0: [1], 1: [], 2: [3], 3: []}
print(LienThong(dt4))  