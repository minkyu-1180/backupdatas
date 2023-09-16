# 백준 13305. 주유소
import sys
sys.stdin = open("bj13305input.txt")

T = int(input())
for tc in range(T):
    N = int(input()) # 도시 개수
    city_dist = list(map(int, input().split())) # i번 ~ i+1번 도시 거리차
    price_per_liter = list(map(int, input().split())) # i번 도시에서의 리터당 가격

    result = 0
    min_price = 1000000000

    for i in range(N-1):
        now_price = price_per_liter[i]
        dist = city_dist[i]
        if min_price > now_price:
            min_price = now_price
        result += min_price * dist
    print(result)