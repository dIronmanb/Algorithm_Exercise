# -*- coding: utf-8 -*-

import sys

n = int(input())
l = []

for i in range(n):
    l.append(int(sys.stdin.readline()))

for i in sorted(l):
    sys.stdout.write(str(i) + '\n')

# 결론: python은 알고리즘 보다는 sorted를 쓰는 걸...권장