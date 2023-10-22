# 백준 1863. 스카이라인 쉬운거
import sys
sys.stdin = open("bj1863input.txt")

# 고도가 바뀌는 지점 개수 (1<= N<= 50000)
N = int(input())
result = 0 # 결과
stack = []
for _ in range(N):
    x, y = map(int, input().split())

    # y가 0인 경우 : 새로운 건물 집합의 스카이라인이 등장 예정
    if y == 0:
        # 그동안 쌓여있는 개수 추가 후, stack 비워주기
        result += len(stack)
        stack = []
    else:
        if not stack:
            stack.append(y)
        else:
            # 스택이 빌 때까지 비교
            while stack:
                # stack의 top 원소값이 y보다 작거나 같음 -> break
                if stack[-1] <= y:
                    break
                # stack의 top 원소값이 y보다 큼 -> pop후 결과 추가
                stack.pop()
                result += 1
            # while문에서 빠져나온 경우
            # 1. 스택이 비어있거나
            # 2. stack[-1] <= y
            # 이 중, stack[-1]이 y와 같은 값인 경우, 의미 X(자기 건물 만난 것)
            if not stack or stack[-1] < y:
                stack.append(y)
# 마지막에도 사실상 y가 0인 좌표가 추가되는 것이나 마찬가지
# 따라서, 쌓인 stack원소개수 추가
result += len(stack)
print(result)
