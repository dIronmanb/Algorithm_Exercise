# -*- coding: utf-8 -*-
import sys

read = sys.stdin.readline

A = read().rstrip()
T = read().rstrip()
text = T[:]
change = 1

while change:
    change = 0

    print("Loop",text)
    # remove from front
    for i in range(len(T) - len(A) + 1):
        if T[i:i+len(A)] == A:
            text = text[ : i] + text[i + len(A):]
            change += 1
            T = text
            print("Front",text)
            break
        


    if change:
    # remove from back
        for i in range(len(T) - len(A) + 1, 0, -1):
            if T[i+len(A) : i :-1] == A[::-1]:
                text = text[ : i+1] + text[i + 1 +len(A):]
                T = text
                print("Back",text)
                break
    else:
        break


print("Final text is >> ",text)



# 앞에서부터 출력
# for i in range(len(T) - len(A) + 1):
#     print(T[i:i+len(A)])

# 뒤에서부터 출력
# for i in range(len(T) - len(A) + 1, 0, -1):
#     print(T[i+len(A) : i :-1])
# print(A[::-1])


# for i in range(len(T) - len(A) + 1):
#     if T[i:i+len(A)] == A:
#            text = text[ : i] + text[i + len(A):]
#            break
# print(text)



# for i in range(len(T) - len(A) + 1, 0, -1):
#     if T[i+len(A) : i :-1] == A[::-1]:
#         print("정답 T[{}:{}:-1] , A[::-1]".format(len(A) + i,i))
#         text = text[ : i+1] + text[i + 1 +len(A):]
#         break
#     else:
#         print("오답 T[{}:{}:-1] , A[::-1]".format(i,len(A)))
# print(text)
# print(text[::-1])
