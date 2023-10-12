# matplotlib 연습
import matplotlib.pyplot as plt

# 예제1 : x, y가 같을 때
plt.plot([1, 2, 3, 4])
# plt.show() 위의 plot을 하나의 객체로 인식하여 출력
# 안해주면 다음 plot 그림에 남아있음 -> plt.clf() : 기존 plot 지우기

# 예제2 : x, y과 다를 때
x = [1, 2, 3, 4]
y = [1, 4, 8, 16]
plt.plot(x, y)
plt.show()

# 예제3 : 제목 + 각 축의 설명
plt.plot(x, y)
plt.title("Test Graph")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()

# 파일로 이미지 저장하기
# plt.show()를 지우기
# plt.savefig('filename.png')