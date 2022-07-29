# import sys

# sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for test_case in range(1, T + 1):
    
    S = input()
    s = ''
    
    for i in range(len(S)):
        if S[i] == 'p':
            s = 'q' + s

        elif S[i] == 'q':
            s = 'p' + s

        elif S[i] == 'b':
            s = 'd' + s

        elif S[i] == 'd':
            s = 'b' + s


    print(f"#{test_case} {s}")