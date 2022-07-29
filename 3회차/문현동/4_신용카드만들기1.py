# import sys

# sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    
    i = 0
    sum_ = 0
    
    while i < len(N):
        if i % 2:
            sum_ += N[i]
        else:
            sum_ += (N[i] * 2)
        i += 1
        
    print(f"#{test_case} {int(str(10 - int(str(sum_)[-1]))[-1])}") # 혹시 몰라서 마지막에 한 번 더 정수로 바꿔주었다.