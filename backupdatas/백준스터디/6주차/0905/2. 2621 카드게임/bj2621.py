# 백준 2621. 카드게임
import sys
sys.stdin = open("bj2621input.txt")


card_num = dict()
num_c = [0] * 10
num_types = set()
for _ in range(5):
    color, num = input().split()
    if color in card_num:
        card_num[color].append(int(num))
    else:
        card_num[color] = [int(num)]
    num_c[int(num)] += 1
    num_types.add(int(num))
print(card_num)
print(num_c)
print(num_types)
if len(num_types) == 1:
    for i in range(1, 6):
        if num_c[i] == 1:
            for j in range(1, 5):
                if num_c[i+j] != 1:
                    result = 900 + num

'''  
color = []
num = []
for _ in range(5):
    c, n = input().split()
    color.append(c)
    num.append(int(n))

# 카드 5장이 모두 같은 색
if len(set(color)) == 1:
    num.sort()
    for i in range(4):
        # 4
        if num[i+1] - num[i] != 1:
            result = num[4] + 600
            break
    # 1
    else:
        result = num[4] + 900
else:
    types_num = set(num)
    num_count = dict()
    for n in types_num:
        if n not in num_count:
            num_count[n] = num.count(n)

    # 1-4 or 2-3
    if len(types_num) == 2:
        for a, b in num_count:
            # 4개의 숫자가 같을 때
            if a == 1:
                result = b + 800
            elif a == 4:
                result = a + 800
            else:
                if a == 2:
                    result = b * 10 + a + 700
                else:
                    result = a * 10 + b + 700
    #1-2-2, 1-1-3
    elif len(types_num) == 3:
        # 1-2-2
        if 2 in num_count.values:
            lst = []
            for n in types_num:
                if num_count[n] != 1:
                    lst.append(n)
            lst.sort()
            result = 300 + lst[0] + 10 * lst[1]
        # 1-1-3
        else:
            for n in types_num:
                if num_count[n] == 3:
                    result = n + 400

    elif len(types_num) == 4:
        for n in types_num:
            if num_count[n] == 2:
                result = n + 200
    elif len(types_num) == 5:
        num.sort()
        for i in range(4):
            if num[i+1] - num[i] != 1:
                result = num[4] + 100
                break
        else:
            result = num[4] + 500

print(result)
'''