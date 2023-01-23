# 숫자 카드 2

# 정렬, 이분탐색
import sys
read = sys.stdin.readline


def lower_bound(target, data):
    start, end = 0, len(data) - 1
    while (end > start):
        mid = (start + end) // 2
        if data[mid] >= target:
            end = mid
        else:
            start = mid + 1

    return end

def upper_bound(target, data):
    start, end = 0, len(data) - 1
    while(end > start):
        mid = (start + end) // 2
        if data[mid] > target:
            end = mid
        else:
            start = mid + 1
    return end


N = int(input())
cards = [int(i) for i in read().split()]
cards = sorted(cards)
M = int(input())
suggest = [int(i) for i in read().split()]



for idx, val in enumerate(suggest):
    upper = upper_bound(val,cards)
    lower = lower_bound(val,cards)

    # 예외처리: index가 -1인 경우에 대하여
    if upper == N-1 and cards[N-1] == suggest[idx]:
        upper += 1

    print(upper - lower, end=" ")
