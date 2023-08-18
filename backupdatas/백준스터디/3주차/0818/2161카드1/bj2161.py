# 백준 2161. 카드1
import sys
sys.stdin = open("2161input.txt")

N = int(input()) # 1 <= N <= 1000
# 1 ~ N번호가 붙은 N장의 카드
# 1번 카드가 제일 위, N번 카드가 제일 아래(front = 0, rear = N-1)
'''
동작 과정
1. 제일 위에 있는 카드 pop
2. 현재 제일 위에 있는 카드를 가장 밑으로
3. 카드가 한 장 남아있을 때 까지 위의 과정 반복

출력 내용
버린 순서대로 카드 출력(마지막에는 남은 카드 번호 출력)
'''

# enqueue 과정 마침
queue = list(range(1, N+1))
result = []

while len(queue) > 1:
    # 제일 위에 있는 카드 버리기(result에 append)
    result.append(queue.pop(0))
    if len(queue) == 1:
        break
    # 제일 위에 있는 카드를 아래로 가져가기
    queue.append(queue.pop(0))



for card in result:
    print(card, end = ' ')
print(queue[0])
