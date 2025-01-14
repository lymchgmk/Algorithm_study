﻿import time
start_time = time.time()

import sys
sys.stdin = open("최적경로_input.txt", "r")
T = int(input())
def getD(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def perm(n, k, cur_dist):
    global ans
    if cur_dist > ans: return

    if k == n:
        cur_dist += D[A[k]][A[N+1]]
        if cur_dist < ans : ans = cur_dist
    else:
        for i in range(k, n, 1):
            A[k + 1], A[i+1] = A[i+1], A[k + 1]
            perm(n, k+1, cur_dist + D[A[k]][A[k+1]])
            A[k + 1], A[i+1] = A[i+1], A[k + 1]

for tc in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    A = [0] + list(range(1, N+1, 1)) +[N+1]  #회사-고객-집
    P = [(0,0) for _ in range(N+2)]          #좌표
    D = [[0 for _ in range(N+2)] for _ in range(N+2)]  #거리
    ans = 0x7fffffff
    P[0] = (temp[0], temp[1])  # 회사
    P[N+1] = (temp[2], temp[3]) # 집

    idx = 1
    for i in range(4, len(temp), 2): # 고객
        P[idx] = (temp[i], temp[i+1])
        idx += 1

    for i in range(N+1):   #메모이제이션
        for j in range(i+1, N+2, 1):
            D[j][i] = D[i][j] = getD(P[i], P[j])

    perm(N, 0, 0)
    print("#{} {}".format(tc+1, ans))

print(time.time() - start_time, 'seconds')
