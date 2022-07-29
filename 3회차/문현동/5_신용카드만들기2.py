# import sys

# sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = input()
    
    if (N[0] != '3' and N[0] != '4' and N[0] != '5' and N[0] != '6' and N[0] != '9') or (len(N) - N.count('-')) < 16:
        print(f"#{test_case} {0}")
    else:
        print(f"#{test_case} {1}")
        
# 3, 4, 5, 6, 9 가 모두 아니거나, (모두 아니어야 하기 때문에 and 로 구분)
# 전체에서 하이픈 문자의 개수 만큼을 뺀 길이가 16이 안되는 경우, ( 두 조건 중 하나만 안되도 False 이기 때문에 or 로 구분)
# 0 혹은 1 출력