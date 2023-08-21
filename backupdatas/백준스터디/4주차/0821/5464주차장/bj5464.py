# 백준 5464. 주차장
import sys
sys.stdin = open("5464input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    R = [Rs for Rs in range(N)] # N개의 주차 공간 : 각 원소는 무게당 요금
    W = [Wk for Wk in range(M)] # M개의 자동차 : 각 원소는 무게