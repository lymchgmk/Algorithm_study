import sys
sys.stdin = open("6549_히스토그램에서 가장 큰 직사각형.txt", "rt")


input = lambda: sys.stdin.readline().strip()
while True:
    h = list(map(int, input().split()))
    n = h[0]
    if h == [0]:
        break


class SegTree:
    def init(self, node, left, right):
        if left + 1 == right:
            self.tree[node] = self.A[left]
        else:
            mid = (left + right) // 2
            self.tree[node] = self.init(node*2, left, mid) + self.init(node*2 + 1, mid, right)
        
        return self.tree[node]

    
    def __init__(self, N, A):
        self.A = A
        self.tree = [0] * 4 * N
        self.init(1, 0, N)

    
    def sum(self, node, left, right, start, end):
        if start <= left and right <= end:
            return self.tree[node]
        if right <= start or end <= left:
            return 0
        mid = (left + right) // 2
        return self.sum(node * 2, left, mid, start, end) + self.sum(node * 2 + 1, mid, right, start, end)

    
    def update(self, node, left, right, target, value):
        if left <= target < right:
            self.tree[node] += value
            if left + 1 == right:
                return
            
            mid = (left + right) // 2
            self.update(node * 2, left, mid, target, value)
            self.update(node * 2 + 1, mid, right, target, value)

    