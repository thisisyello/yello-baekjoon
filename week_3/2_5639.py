import sys
sys.setrecursionlimit(10**6)

preorder = []
for line in sys.stdin:
    preorder.append(int(line.strip()))

def solve(start, end):
    if start >= end:
        return
    
    root = preorder[start]
    idx = start + 1

    while idx < end and preorder[idx] < root:
        idx += 1

    solve(start + 1, idx)
    solve(idx, end)

    print(root)

solve(0, len(preorder))