# import sys

# sys.stdin = open("_소득불균형.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    income_list = list(map(int, input().split()))
    
    low_income_list = []
    
    for workerS_income in income_list:
        if workerS_income <= sum(income_list) / N: # 평균을 낸 다음 어떤 일꾼의 수입이 그 평균보다 적으면
            low_income_list.append(workerS_income) # 그 작은 사람들을 '적은 수입 리스트' 에 추가
    
    print(f"#{test_case} {len(low_income_list)}")