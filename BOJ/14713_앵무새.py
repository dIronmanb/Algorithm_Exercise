import sys
from collections import deque
read = sys.stdin.readline


N = int(read().rstrip())
corpus = []
for i in range(N):
    corpus.append(deque(a for a in read().split()))
#print(corpus)

sentence = deque(i for i in read().split())


for word in list(sentence):
    for i in range(N):
        if corpus[i] and word == corpus[i][0]:
            corpus[i].popleft()
            sentence.popleft()


# print(corpus)
is_possible = True

if sentence:
    is_possible = False
else:
    for i in range(N):
        if corpus[i]:
            is_possible = False
            break

if is_possible:
    print("Possible")
else:
    print("Impossible")