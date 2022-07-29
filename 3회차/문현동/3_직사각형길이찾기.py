# import sys

# sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    
    if len(set(N)) < 2: # 어떤 값들의 중복값을 없앨 때, 값이 하나만 남는다면 그것은 정사각형이므로 0번째 값이 곧 변의 길이이다.
        piece = N[0]
    else:
        for i in N: # 값이 두개 이상 나온다면 그것은 직사각형이므로 같은 값의 개수가 한 개인 값이 곧 나머지 변의 길이이다.
            if N.count(i) < 2:
                piece = i
    
    print(f"#{test_case} {piece}")