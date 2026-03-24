# matplotlib : 플로팅 라이브러리. 그래프 생성을 위한 다양한 함수를 제공
# 시각화의 중요성
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'AppleGothic'   # Mac 한글 폰트
plt.rcParams['axes.unicode_minus'] = False    # 마이너스 깨짐 방지


x = ["서울", "인천", "수원"]
# x = ("서울", "인천", "수원")
# x = {"서울", "인천", "수원"}                      set 타입은 쓸 수 없다.
y = [5, 3, 7]

plt.xlim([-1,3])
plt.ylim([0,10])
# tick 설정 : y축의 라벨을 인위적으로 표시
plt.yticks(list(range(0,11,3)))


plt.plot(x,y)
plt.show()

data = np.arange(1,11,2)
plt.plot(data)
x = [0,1,2,3,4]
for a,b in zip(x,data):
    plt.text(a,b,str(b))
plt.show()

x = np.arange(10)
y = np.sin(x)
print(x,y)
# plt.plot(x,y)
plt.plot(x,y,'go--',linewidth=2, markersize=12)
plt.show()

# hold : 복수의 plot으로 여러개의 차트를 겹쳐 그림
x = np.arange(0, np.pi * 3, 0.1)
print(x)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure(figsize=(10,5))              # 그래프 전체 크기(w,h)
plt.plot(x,y_sin,'r')                   # 선 그래프
plt.scatter(x,y_cos)                    # 산점도
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('sine & cosine')              
plt.legend(['sine', 'cosine'])
plt.show()
print()
# sublplot : 하나의 figure를 여러개의 Axes(plot)으로 나누기
plt.subplot(2,1,1)      # 1행
plt.plot(x,y_sin)
plt.title('sine')
plt.subplot(2,1,2)      # 2행
plt.plot(x,y_cos)
plt.title('cosine')
plt.show()


print()
irum = ['a', 'b', 'c', 'd', 'e']
kor = [80, 50, 70, 70, 90]
eng = [60, 70, 80, 90, 100]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bo--')
plt.ylim([50,100])
plt.title('시험 점수')
plt.legend(['국어', '영어'], loc = 4)               # loc = 'best'
plt.grid(True)                                  # 궤선

fig = plt.gcf()
plt.show()
fig.savefig('plot1.png')

from matplotlib.pyplot import imread                # Flask에서 이미지 쓰는 법 지금처럼 저장해서 static 폴더에 저장한다 img.src -> 정적이다
img = imread('plot1.png')                           # chart.js를 쓴다
plt.imshow(img)
plt.show()


