# IM 대비 3. 백준 2309 일곱 난쟁이
import sys
sys.stdin = open("2309일곱난쟁이input.txt")

arr = [0] * 9
for i in range(9):
    arr[i] = int(input())

# 7개의 원소로 이루어진 부분집합 중, 부분집합의 합이 100인 케이스 찾기
# 여러개 있으면 한 가지 경우만 출력
for i in range(1 << 9):
    subset = []
    for j in range(9):
        if i & (1 << j):
            subset.append(arr[j])
    # 부분집합 생성 결과 원소개수 7인 경우
    if len(subset) == 7:
        sum_seven = 0
        for h in subset:
            sum_seven += h
        # 일곱난쟁이의 키의 합이 100인 경우 종료
        if sum_seven == 100:
            subset.sort() # 오름차순 정렬
            break
for h in subset:
    print(h)


