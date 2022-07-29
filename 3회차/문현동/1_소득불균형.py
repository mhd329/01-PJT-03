# import sys

# sys.stdin = open("_소득불균형.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    income_list = list(map(int, input().split()))
    
    low_income_list = []
    
    for workerS_income in income_list:
        if workerS_income <= sum(income_list) / N:
            low_income_list.append(workerS_income)
    
    print(f"#{test_case} {len(low_income_list)}")