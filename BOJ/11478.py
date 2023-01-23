# 사로 다른 부분 문자열의 개수

import sys
read = sys.stdin.readline


string = read().rstrip()

result = set()

for k in range(len(string)):
    for i in range(len(string)-k):
        result.add(string[i:i+k+1])

print(len(result))



# for i in range(len(string)):
#     result.add(string[i:i+1])
#
# for i in range(len(string)-1):
#     result.add(string[i:i+2])
#
# for i in range(len(string)-2):
#     result.add(string[i:i+3])
# a = ['a', 'b', 'a', 'b', 'c', 'ab', 'ba', 'ab', 'bc', 'aba', 'bab', 'abc', 'abab', 'babc', 'ababc']