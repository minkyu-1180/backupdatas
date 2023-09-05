# 백준 2621. 카드게임
import sys
sys.stdin = open("bj2621input.txt")

num_counts_dict = {}
num_count = [0 for _ in range(10)]
num_type = set()

for _ in range(5):
    color, num = input().split()
    if color in num_counts_dict:
        num_counts_dict[color].append(int(num))
    else:
        num_counts_dict[color] = [int(num)]
    num_count[int(num)] += 1
    num_type.add(int(num))


def same_color(num_counts_dict):
    if len(num_counts_dict) == 1:
        return True
    return False


def isContinue(num_count):
    index = 0
    for i in range(1, 10):
        if num_count[i] != 1:
            if num_count[i] != 0:
                return False
        else:
            if index == 0:
                index = i
            else:
                if index + 1 != i:
                    return False
                else:
                    index = i
    return True


def same_number(num_count):
    count = sorted(num_count, reverse=True)

    if count[0] == 4:
        return 8
    elif count[0] == 3:
        if count[1] == 2:
            return 7
        else:
            return 4
    elif count[0] == 2:
        if count[1] == 2:
            return 3
        else:
            return 2


num_type = sorted(list(num_type))
result = 100 + num_type[-1]

if same_color(num_counts_dict):
    # case 1
    if isContinue(num_count):
        result = max(result, 900 + num_type[-1])
    # case 4
    else:
        result = max(result, 600 + num_type[-1])
else:
    # case 5
    if isContinue(num_count):
        result = max(result, 500 + num_type[-1])


same_number = same_number(num_count)
if same_number == 8:  # case 2
    result = max(result, 800 + num_count.index(4))
elif same_number == 7:  # case 3
    result = max(result, 700 + num_count.index(3) * 10 + num_count.index(2))
elif same_number == 4:  # case 6
    result = max(result, 400 + num_count.index(3))
elif same_number == 3:  # case 7
    num1 = num_count.index(2)
    num2 = num_count.index(2, num1 + 1, 10)
    result = max(result, 300 + num2 * 10 + num1)
elif same_number == 2:  # case 8
    result = max(result, 200 + num_count.index(2))

print(result)