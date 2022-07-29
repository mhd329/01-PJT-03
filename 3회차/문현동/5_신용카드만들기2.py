# import sys

# sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = input()
    
    if N[0] != '3' and N[0] != '4' and N[0] != '5' and N[0] != '6' and N[0] != '9' or len(N) - N.count('-') < 16:
        print(f"#{test_case} {0}")
    else:
        print(f"#{test_case} {1}")