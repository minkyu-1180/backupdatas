# IM 대비 10. 백준 2628 종이자르기
import sys
sys.stdin = open("2628종이자르기input.txt")

N, M = map(int, input().split())
K = int(input())

result = []
for _ in range(K):
    rc, idx = map(int, input().split())
    print(rc, idx)

print(result)

'''
def cut(rc, idx, N, M):
    if rc == 0: # 가로로 자르기
        if result == []:
            result.append([[0, idx], [0, M]])
            result.append([[idx, N], [0, M]])
        else:
            for info in result:
                row_info, col_info = info[0], info[1]
                if idx in range(row_info[0], row_info[1]):
                    info1 = [[row_info[0], idx], col_info]
                    info2 = [[idx, row_info[1]], col_info]
                    result.remove(info)
                    result.append(info1)
                    result.append(info2)
    elif rc == 1:
        if result == []:
            result.append([[0, N], [0, idx]])
            result.append([[0, N], [idx, M]])
        else:
            for info in result:
                row_info, col_info = info[0], info[1]
                if idx in range(col_info[0], col_info[1]):
                    info1 = [row_info, [col_info[0], idx]]
                    info2 = [row_info, [idx, col_info[1]]]
                    result.remove(info)
                    result.append(info1)
                    result.append(info2)
'''
