# Perceptron : sklearn이 제공하는 단층신경망(뉴런, 노드)
# 이항분류 가능

# 실습1) 논리회로 분류
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

feature = np.array([[0,0], [0,1], [1,0], [1,1]])
print(feature)
# label = np.array([0,0,0,1])         # and
label = np.array([0,1,1,1])         # or
# label = np.array([0,1,1,0])         # xor 이건 안된다. 50%만 맞출수 있다. 선형모델이기 때문이다.



ml = Perceptron(max_iter=100).fit(feature, label)   # max_iter(epoch, 학습횟수)
print(ml)
pred = ml.predict(feature)
print('pred : ', pred)
print('acc : ', accuracy_score(label, pred))

print('-------------------------')
# Perceptron은 딥러닝의 경사하강법과는 달리 틀린 것만 고치는 알고리즘
# 흐름 : 예측 -> 맞았는지 확인 -> 틀리면 weight를 갱신, 맞으면 통과 -> 이 과정 반복
# 선형회귀식 사용(Logistic Regression을 기반으로 함)
# -input에 대한 가중치 합 계산 후 실제값과 예측값 비교(Loss function)
# -이어서 역전파를 통해 w를 갱신하기를 max_iter만큼 반복함

# 실습2) 일반 자료 분류
x = np.array([
    [2,3],
    [3,3],
    [1,1],
    [5,2],
    [6,1]
])

y = np.array([1,1,1,-1,-1])
model = Perceptron(max_iter=100, eta0=0.1, random_state=52)            # eta = learning rate
model.fit(x,y)
pred = model.predict(x)
print('예측값 : ', pred)
print('실제값 : ', y)
print('정확도 : ', accuracy_score(y, pred))

# parameter
print('가중치(W) : ', model.coef_)
print('바이어스(b) : ', model.intercept_)

# 결정 경계(w1*x1 + w2*x2 + b) 시각화
import matplotlib.pyplot as plt
plt.scatter(x[:,0], x[:,1], c=y, cmap='bwr')
