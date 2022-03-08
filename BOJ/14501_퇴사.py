import sys
read = sys.stdin.readline


def is_possible(now):
    global money
    if now >= days: return

    next_day = now + work_table[now][0]

    if next_day > days:
        impossible[now] = True
        return

    else:
        money += work_table[now][1]
        is_possible(i)


days = int(read())
work_table = []
price_table = []
money = 0
impossible = [0] * days

for i in range(days):
    work_table.append([int(i) for i in read().split()])


for i in range(days):
    money = 0
    if impossible[i]:
        continue
    is_possible(i)
    price_table.append(money)

print(price_table)
