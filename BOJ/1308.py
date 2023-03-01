import sys
read = sys.stdin.readline


# 윤년: 4로 나누어 떨어지는 해 -> 366일 (2월 29일)
# 평년: 100으로 나누어 떨어지는 해 -> 365일
# 윤년: 400으로 나누어 떨이지는 해 -> 366일
# 나머지는 평년

s_y, s_m, s_d = [int(i) for i in read().split()]
e_y, e_m, e_d = [int(i) for i in read().split()]

origin = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yun = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]




if s_y % 4 == 0:
    if s_y % 100 == 0:
        if s_y % 400 == 0:
            # 윤년
            front = 366 - (sum(yun[:s_m]) + s_d)
            if s_y == e_y:
                front = 366 - front
        else :
            # 평년
            front = 365 - (sum(origin[:s_m]) + s_d)
            if s_y == e_y:
                front = 365 - front
    else:
        # 윤년
        front = 366 - (sum(yun[:s_m]) + s_d)
        if s_y == e_y:
            front = 366 - front
else:
    # 평년
    front = 365 - (sum(origin[:s_m]) + s_d)
    if s_y == e_y:
        front = 365 - front

if e_y % 4 == 0:
    if e_y % 100 == 0:
        if e_y % 400 == 0:
            # 윤년
            back = sum(yun[:e_m]) + e_d
        else:
            # 평년
            back = sum(origin[:e_m]) + e_d
    else:
        # 윤년
        back = sum(yun[:e_m]) + e_d
else:
    # 평년
    back = sum(origin[:e_m]) + e_d


years, cnt = 0, 0
for year in range(s_y + 1, e_y, 1):  # s_y+1년부터 e_y-1년까지
    yun_flag = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # 윤년
                yun_flag = True
            else:
                # 평년
                yun_flag = False
        else:
            # 윤년
            yun_flag = True
    else:
        # 평년
        yun_flag = False

    if yun_flag:
        # 윤년이면
        cnt += 366
        years += 1
    else:
        # 평년이면
        cnt += 365
        years += 1

def get_n_year_day(start_year, n):
    year_day_n = 0

    for year in range(start_year, start_year+n):
        if year % 400 == 0:
            year_day_n += 366
        elif year % 100 == 0:
            year_day_n += 365
        elif year % 4 == 0:
            year_day_n += 366
        else:
            year_day_n += 365
    return year_day_n


if front + back + cnt >= get_n_year_day(s_y, 1000):
    print("gg")
else:
    if s_y == e_y:
        print(f"D-{back-front}")
    else:
        print(f"D-{front + back + cnt}")
    print(f"front:{front} / back:{back} / cnt:{cnt} / years:{years}")

'''
    알고리즘
         [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
    평년: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    윤년: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    - 오늘의 해가 몇 윤년인지 평년인지를 판단
        - if 윤년:
            366일 가지고 처리
        - if 평년:
            365d일 가지고 처리
    
    if s_y가 윤년:
        if s_m월 s_d일이 2월 29일보다 늦는다면:
            front = 366 - ([평년] (s_m월 s_d일까지의 합) + 1)
        else:
            front = 366 - ([평년] (s_m월 s_d일까지의 합))
        
    if e_y가 윤년:
        if: e_m월 e_d일이 2월 29일보다 빠르다면:
            back = [평년] (e_m월 e_d일까지의 합)
        else:
            back = [평년] (e_m월 e_d일까지의 합) + 1
    
    years, cnt = 0, 0
    for year in (s_y+1, e_y): # s_y+1년부터 e_y-1년까지
        if year이 윤년:
            cnt += 366
            years += 1
        else: # 평년
            cnt += 365
            years += 1
            
    if years >= 1000:
        print("gg")
    else:
        print(f"D-{front + back + cnt}')

'''