# import sys

# sys.stdin = open("_최빈수구하기.txt")


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    score_list = list(map(int,input().split()))
    
    score_dict = {}
    
    for score in score_list:
        if score in score_dict:
            score_dict[score] += 1
        else:
            score_dict[score] = 1 # 여기까지는 우리가 예전에 해 왔던 '딕셔너리로 빈도 찾기' 구현과 같다.
            
    frequency_list = []
    most_frequency_list = []
    
    for v in score_dict.values(): # 어떤 수의 빈도값을 빈도 리스트에 추가
        frequency_list.append(v)
        
    for i in score_dict:
        if score_dict[i] == max(frequency_list): # 딕셔너리의 어떤 값이 빈도 리스트의 최대값 (제일 많이 나왔다는 뜻) 인 경우 '제일 많은 빈도 리스트' 에 추가
            most_frequency_list.append(i)
        
    print(f"#{N} {max(most_frequency_list)}") # '제일 많은 빈도 리스트' 에서 숫자가 제일 큰 것을 출력