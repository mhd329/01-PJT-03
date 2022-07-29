# import sys

# sys.stdin = open("_암호문1.txt")

# 암호문은 명령어가 여러 개일 경우, 맨 처음 명령어를 실행하고 오리지널을 바꾼 다음 두 번째 명령어를 실행한다.

for test_case in range(1, 11):
    
    length_of_cryptogram = int(input()) # 암호문의 길이 (사실상 쓰지 않았다.)
    original_cryptogram = input().split() # 원본 암호문
    num_of_command = int(input()) # 커맨드의 수 (사실상 쓰지 않았다.)
    insert_command_list = list(input().split('I')) # 커맨드 리스트를 입력받고 I 로 구분하여 다시 리스트로 만듦
    
    command_list = []
    for i in insert_command_list:
        command_list.append(i.split()) # 한 번의 명령어세트가 들어가있는 리스트
    
    command_list.remove([]) # I 가 있던 자리는 빈 리스트가 되기 때문에 편의상 빈 리스트를 없애주었다. 즉 형태는 x y s
    
    for command in command_list: # 명령어 리스트의 각 명령어 원소에 대하여,
        for j in range(int(command[1])):
            # [1] 에 해당하는 명령어의 범위만큼의 j 에 대하여,
            # 즉 몇 개 ( j 개의 ) 의 암호를 어디에 ( int(command[0]) + j 번째에, ) 넣을지 여기서 결정됨.
            original_cryptogram.insert(int(command[0]) + j, command[j + 2])
            # 원본 리스트에 insert 한다. 무엇을? >>>  int(command[0]) + j 라는 위치에, command[j + 2] 라는 원소를.
            # 위치를 결정할 때, int(command[0]) 라고 하지 않고 + j 를 해 준 이유는,
            # insert 메서드는 가리키고 있는 자리의 앞에 insert 를 하기 때문에,
            # int(command[0]) + j 를 하였다. 그랬을 때 결과를 보면,
            # j 가 하나씩 올라갈 때마다 insert 대상의 자리가 한 자리씩 뒤로 밀리면서, 해당 수의 뒷자리에 insert 되는 효과가 난다.
    print(f"#{test_case} {' '.join(original_cryptogram[:10])}")