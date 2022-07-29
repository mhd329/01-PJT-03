# import sys

# sys.stdin = open("_암호문1.txt")

# 암호문은 명령어가 여러 개일 경우, 맨 처음 명령어를 실행하고 오리지널을 바꾼 다음 두 번째 명령어를 실행한다.

for test_case in range(1, 11):
    
    length_of_cryptogram = int(input())
    original_cryptogram = input().split()
    num_of_command = int(input())
    insert_command_list = list(input().split('I'))
    
    command_list = []
    for i in insert_command_list:
        command_list.append(i.split())
    
    command_list.remove([])
    
    for command in command_list:
        for j in range(int(command[1])):
            original_cryptogram.insert(int(command[0]) + j, command[j + 2])

    print(f"#{test_case} {' '.join(original_cryptogram[:10])}")