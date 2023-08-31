import sys
sys.stdin = open('최대상금input.txt')

# x번 idx에 재배치한 값 추가
def change(arr, n, x):
    case = int(''.join(arr))
    # 이미 있을 경우 x
    if case in cases[x]:
        return
    # 새로운 k번 교환의 값 -> 추가
    else:
        cases[x].append(case)

    # 더 이상 교환 불가 시 종료
    if x == k:
        return

    for i in range(n-1):
        for j in range(i + 1, n):
            # 모든 자리를 교환하여 change 진행
            arr[i], arr[j] = arr[j], arr[i]
            change(arr, n, x+1)
            # 복원
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())

for test_case in range(1, T + 1):
    N, K = input().split()
    arr = list(N)
    n = len(arr)
    k = int(K)

    # k번 idx 에 들어가는 값 : k-1번 idx에 들어있는 값의 두 자리를 선택하여 교환한 값
    cases = [[] for _ in range(k+1)]
    change(arr, n, 0) # 0번 idx에 들어가는 값 : 원본 숫자

    result = max(cases[k]) # 가장 마지막 케이스에 있는 값들 중 가장 큰 값

    print(f'#{test_case} {result}')