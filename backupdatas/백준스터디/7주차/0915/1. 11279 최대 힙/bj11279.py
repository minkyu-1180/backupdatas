# 백준 11279. 최대 힙
import sys
sys.stdin = open("bj11279input.txt")
N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    # 1. heapqpush
    if x > 0:
        heap.append(x)
        child_idx = len(heap)-1
        while child_idx != 0:
            if child_idx % 2:
                parent_idx = child_idx // 2
            else:
                parent_idx = child_idx // 2 - 1

            if heap[parent_idx] > heap[child_idx]:
                break
            heap[parent_idx],heap[child_idx] = heap[child_idx], heap[parent_idx]
            child_idx = parent_idx

    # 2. heapqpop
    else:
        if heap:
            print(heap[0])
            if len(heap) >= 2:
                heap[0], heap[-1] = heap[-1], heap[0] # 가장 끝 인덱스 땡겨오기
                heap.pop()
                parent_idx = 0
                while parent_idx * 2 + 1 <= len(heap) - 1:
                    left_child_idx = parent_idx * 2 + 1
                    right_child_idx = (parent_idx + 1) * 2
                    if len(heap) - 1 < right_child_idx:
                        if heap[parent_idx] > heap[left_child_idx]:
                            break
                        heap[parent_idx], heap[left_child_idx] = heap[left_child_idx], heap[parent_idx]
                        parent_idx = left_child_idx
                    else:
                        if heap[left_child_idx] > heap[right_child_idx]:
                            max_child_idx = left_child_idx
                        else:
                            max_child_idx = right_child_idx
                        if heap[parent_idx] > heap[max_child_idx]:
                            break
                        heap[parent_idx], heap[max_child_idx] = heap[max_child_idx], heap[parent_idx]
                        parent_idx = max_child_idx
            else:
                heap.pop()

        else:
            print(0)

            '''
     '''