# 백준 1615. 교차개수세기
import sys
sys.stdin = open("bj1615input.txt")


def update(node, left, right, index):
    if index > right or index < left:
        return

    segment_tree[node] += 1
    if left == right:
        return

    mid = (left+right)//2
    update(2*node, left, mid, index)
    update(2*node+1, mid+1, right, index)

def query(node, left, right, start, end):
    if start > right or end < left:
        return 0 # 0개 반환
    if start <= left and right <= end:
        return segment_tree[node]
    mid = (left + right)//2
    return query(2*node, left, mid, start, end) + query(2*node+1, mid+1, right, start, end)

# N : 정점의 쌍(1 <= N <= 2000)
# M : 간선의 개수(1 <= M <= N(N-1)/2)
N, M = map(int, input().split())
edges = []
for _ in range(M):
    # 왼쪽 그룹의 i번 정점과 오른쪽 그룹의 j번 정점을 연결하는 간선이 있다
    i, j = map(int, input().split())
    edges.append((i, j))

edges.sort(key=lambda x : (x[0], x[1]))
# print(edges)
segment_tree = [0] * (4 * N)

result = 0
for i, j in edges:
    # i -> j 간선이랑 교차되는 간선 개수 구하기
    # i기준으로 j ~ N-1 보기
    result += query(1, 1, N, j+1, N)
    update(1, 1, N, j)
    # print(segment_tree)
print(result)

# N,M = map(int,input().split())
# # h = int(math.ceil(math.log2(N)))
# tree = [0]*(4 * N)
#
# edge = []
# for _ in range(M):
#     u,v = map(int,input().split())
#     edge.append((u,v))
#
# edge.sort(key=lambda x:(x[0],x[1]))
#
# def update(left,right,node,index,val):
#     if index>right or index<left:
#         return
#     tree[node]+=val
#     if left!=right:
#         mid = (left+right)//2
#         update(left,mid,node*2,index,val)
#         update(mid+1,right,node*2+1,index,val)
#
# def query(left,right,node,qLeft,qRight):
#     if qLeft>right or qRight<left:
#         return 0
#
#     if qLeft<=left and right<=qRight:
#         return tree[node]
#
#     mid = (left+right)//2
#     return query(left,mid,node*2,qLeft,qRight)+query(mid+1,right,node*2+1,qLeft,qRight)
#
# ans = 0
# for u,v in edge:
#     ans+=query(0,N-1,1,v,N-1)
#     update(0,N-1,1,v-1,1)
#     print(tree)
# print(ans)