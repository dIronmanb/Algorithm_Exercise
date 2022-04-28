# BOJ 알고리즘

## 1. 정렬
- 선택정렬
- 퀵정렬
- 병합정렬
- 배열 인덱스에 바로 넣는 정렬

## 2. BFS, DFS
- 시간에 따라 주변의 영향을 끼친다면 BFS사용
- 아니라면 DFS


## 3. Queue, Stack
- Queue에서 Deque를 주로 사용
- stack의 pop, push로 해결하는 건 list로

## 4. DP: Dynamic Programming - 동적계획법
- 배열을 미리 생성하여 연산값을 저장 -> 배열에 저장된 값으로 다시 연산
- 보통 점화식으로 문제를 품 
  ```
    # Exmanle
    # 전체 가치 = max(오늘 일한 것의 가치, 내일 일한 것의 가치)
    # total_val = max(today_val, tomorrow_val)
  ```

## 5. 그래프
- DFS, BFS문제의 기반이 됨


## 6. 최소 신장 트리
- 다익스트라
- 플루이드
- 크루스칼
- 벨만 최적 방정식

## 7. 비트마스킹
- 임베디드에서 값을 변환할 때 가장 빠른 속도롤 처리할 수 있음.