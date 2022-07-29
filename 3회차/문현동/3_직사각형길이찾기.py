# import sys

# sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    
    if len(set(N)) < 2:
        piece = N[0]
    else:
        for i in N:
            if N.count(i) < 2:
                piece = i
    
    print(f"#{test_case} {piece}")