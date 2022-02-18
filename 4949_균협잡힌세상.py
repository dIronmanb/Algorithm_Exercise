# -*- coding: utf-8 -*-
import sys
read = sys.stdin.readline

result = []

while True:

    paragraph = read().rstrip()
    
    if paragraph == ".":
        break

    stack = []
    failed = False
    for i in paragraph:

        if i == '(' or i == '[':
            stack.append(i)
        
        elif i == ']':
            if stack and stack.pop() == '[':
                pass
            else:
                failed = True
                break
        
        elif i == ')':
            if stack and stack.pop() == '(':
                pass
            else:
                failed = True
                break
    
    if failed:
        result.append("no")
    elif not stack:
        result.append("yes")

for i in result:
    print(i)

    # round_brackets = []
    # square_brackets = []
    # output = True

    # for i in paragraph:
        
    #     if i == '(':
    #         round_brackets.append(i)     
    #     elif i == '[':
    #         square_brackets.append(i)

    #     elif i == ')':
    #         if round_brackets:
    #             if round_brackets.pop() != '(':
    #                 output = False
    #                 break
    #         else:
    #             output = False
    #             break

    #     elif i == ']':
    #         if square_brackets:
    #             if square_brackets.pop() != '[':
    #                 output = False
    #                 break
    #         else:
    #             output = False
    #             break

                


    # if not output:
    #     print("no")
    # elif round_brackets or square_brackets:
    #     print("no")
    # else:
    #     print("yes")

    
# 괄호 안에 있는 문자열도 균형을 이루어야 한다.