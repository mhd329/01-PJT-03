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
            score_dict[score] = 1
            
    frequency_list = []
    most_frequency_list = []
    
    for v in score_dict.values():
        frequency_list.append(v)
        
    for i in score_dict:
        if score_dict[i] == max(frequency_list):
            most_frequency_list.append(i)
        
    print(f"#{N} {max(most_frequency_list)}")