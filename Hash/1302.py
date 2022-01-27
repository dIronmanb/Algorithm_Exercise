import sys
input = sys.stdin.readline

N = int(input())
book_list = {}


for _ in range(N):
    name = input().rstrip()
    if name in book_list.keys():
            book_list[name] += 1
    else:
        book_list[name] = 0
        
name = [key for key, value in book_list.items() if value == max(book_list.values())]
name.sort()


print(name[0])


#print(book_list[max(book_list.values())])