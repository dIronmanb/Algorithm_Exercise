# 크로아티아 알파벳

import sys
read = sys.stdin.readline

string = [char for char in read().rstrip()]
s_cnt = 0

for idx, i in enumerate(string):

    if idx == len(string)-1:
        break

    elif i == 'c':
        if string[idx+1] in ['=', '-']:
            s_cnt += 1

    elif i == 'd' and string[idx+1] == '-':
        s_cnt += 1

    elif i == 'l' and string[idx+1] == 'j':
        s_cnt += 1

    elif i == 'n' and string[idx+1] == 'j':
        s_cnt += 1

    elif i == 's' and string[idx+1] == '=':
        s_cnt += 1

    elif i == 'z' and string[idx+1] == '=' and string[idx-1] != 'd':
        s_cnt += 1

    elif idx < len(string)-2 and i=='d' and string[idx+1] == 'z' and string[idx+2] == '=':
        s_cnt += 2

print(len(string) - s_cnt)
