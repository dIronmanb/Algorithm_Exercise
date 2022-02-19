import sys
read = sys.stdin.readline

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
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                failed = True
                break
        
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                failed = True
                break
    
    print("no" if failed or(stack) else "yes")
    # if failed:
    #     result.append("no")
    # elif not stack:
    #     result.append("yes")
        