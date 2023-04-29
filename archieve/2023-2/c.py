n = int(input())

seen = set()
adj = [[]]
corner = set()

num_corner = 0

def fail():
    print("-1")
    exit(0)

for i in range(1,n+1):
    line = input()
    adj.append(list(map(int, line.split()))[1:])
    if len(adj[-1]) == 2:
        corner.add(i)
    if len(adj[-1]) > 4:
        fail()
    if len(adj[-1]) < 2:
        fail()

if len(corner) != 4:
    fail()

def make_row(grid, first):
    grid.append([])
    grid[-1].append(first)
    seen.add(first)
    #print(grid, first)
    end_cnt = len(adj[first])
    while(len(seen) < n):
        bst = -1
        for nxt in adj[grid[-1][-1]]:
            if nxt in seen:
                continue
            if len(grid) != 1 and nxt not in adj[grid[-2][len(grid[-1])]]: continue
            if bst == -1 or len(adj[bst]) > len(adj[nxt]):
                bst = nxt
        if bst != -1:
            grid[-1].append(bst)
            seen.add(bst)
        else:
            1/0
        if len(adj[grid[-1][-1]]) == end_cnt:
            return

dr = [0,1,0,-1]
dc = [1,0,-1,0]
def check(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid_adj = set()
            for d in range(4):
                nr = row + dr[d]
                nc = col + dc[d]
                if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                    grid_adj.add(grid[nr][nc])
            if grid_adj != set(adj[grid[row][col]]):
                return False
    return True

first = next(iter(corner))
grid = []
while True:
    #print(grid)
    try:
        make_row(grid, first)
    except:
        fail()
    if len(seen) == n:
        break
    for nxt in adj[grid[-1][0]]:
        if nxt not in seen:
            first = nxt
            break
    else:
        fail()

if not check(grid):
    fail()
    
print(len(grid), len(grid[0]))
for row in grid:
    print(" ".join(map(str, row)))