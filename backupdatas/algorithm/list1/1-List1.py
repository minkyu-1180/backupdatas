'''
sw academy
파이썬 sw문제해결 기본 - list1
'''
# 예제
T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f'#{t}', *arr)
print()

# 6차시 1일차 - min max
T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min = arr[0]
    max = arr[0]
    for ele in arr:
        if min > ele:
            min = ele
        elif max < ele:
            max = ele
    result = max - min
    print(f'#{t} {result}')


# 과제 1
'''
암호코드 규칙
1. 8개의 숫자로 이루어짐
2. 앞 7자 : 상품 고유 번호 / 마지막 자리 : 검증 코드
- 검증 코드 계산 : (홀수 자리 합 X 3 + 짝수 자리 합 + 검증 코드)%10 == 0
 
입력
T개의 테스트 케이스가 이어져서 주어진다
'''

