class LinearQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    # 포화
    def is_full(self):
        return self.rear == self.size #

    # 공백상태
    def is_empty(self):
        return self.front == self.rear

    # enqueue
    def enqueue(self, item):
        if self.is_full():
            print('Queue is Full Now!')
            return

        # 메모리 낭비 줄이는 법
        elif self.is_empty():
            # 비어있을 경우, front / rear 초기화
            self.front = self.rear = 0
        self.queue[self.rear] = item
        self.rear += 1




    def dequeue(self):
        if self.is_empty():
            print('Queue is Empty Now!')
            return
        # front 위치의 item 반환
        item = self.queue[self.front]

        # 값이 하나만 남은 경우
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = self.front + 1
        return item


queue = LinearQueue(5)
print(queue.queue) # [None, None, None, None, None]
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6) # Queue is Full Now!
print(queue.queue) # [1, 2, 3, 4, 5]


print(queue.dequeue()) # 1
print(queue.dequeue()) # 2
print(queue.dequeue()) # 3
print(queue.dequeue()) # 4
print(queue.dequeue()) # 5
print(queue.dequeue()) # Queue is Empty Now!


'''
class CircleQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = 0
        
        def 
'''