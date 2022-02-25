# -*- coding: utf-8 -*-
import sys
read = sys.stdin.readline


N = int(read())
F = int(read())


new_N = N + (F - (N % F))

while True:
    new_N = new_N - F
    if new_N < 100 or str(new_N)[-3] != str(N)[-3]:
        break

print(str(new_N + F)[-2:])