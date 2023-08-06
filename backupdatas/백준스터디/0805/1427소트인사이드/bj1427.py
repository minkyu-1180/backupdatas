# 1427. 소트인사이드
arr = list(map(int, str(input())))
for i in range(len(arr)-1, 0, -1):
    for j in range(i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for num in arr:
    print(num, end = "")