# 전통적인 방법의 선형회귀(기계학습 중 지도학습에 해당한다.)
# 각 데이터에 대한 잔차제곱합이 최소가 되는 추세선(회귀선)을 만들고,
# 이를 통해 독립변수가 종속변수에 얼마나 영향을 주는지 인과관계를 분석
# 독립변수 : 연속형, 종속변수 : 연속형 - 두 변수는 상관관계 및 인과관계가 있어야 한다.

import statsmodels.api as sm
from sklearn.datasets import make_regression
import numpy as np

np.random.seed(12)

# 모델 맛보기
# 방법 1 : make_regression 사용. model 생성
x,y,coef = make_regression(n_samples=50, n_features=1, bias=100, coef = True)        # bias를 주지 않으면 default로 원점을 지난다.(절편)

print(x)            # [[-1.70073563] [-0.67794537] [ 0.31866529]
print(y)            # -52.17214291   39.34130801  128.51235594  112.42316554  147.88091341
print()
print(coef)


xx = x 
yy = y
# y = wx + b    y^ = 89.47430739278907*x +100
y_pred = 89.47430739278907*(-0.67794537) + 100
print('예측값 : ', y_pred)

print('\n방법2 : LinearRegression 사용. model 생성')
from sklearn.linear_model import LinearRegression
model = LinearRegression()
fit_model = model.fit(xx,yy)        # 최소제곱법으로 기울기, 절편을 구한다.
print('기울기(slope) : ', fit_model.coef_)              # [89.47430739]
print('절편(bias) : ', fit_model.intercept_)            # 100.0

y_newpred = fit_model.predict(xx[[0]])                # 2차원 배열로 학습해서 2차원 배열로 넣어줘야 한다.
print('예측값1 : ', y_newpred)

y_newpred2 = fit_model.predict(np.array([[0.12345],[0.3],[0.5]]))                # 2차원 배열로 학습해서 2차원 배열로 넣어줘야 한다.
print('예측값2 : ', y_newpred2)

print('\n방법 3 : ols 사용. model 생성')
# 잔차 제곱합(RSS)을 최소화하는 가중치 벡터를 행렬 미분으로 구하는 방법
import statsmodels.formula.api as smf
import pandas as pd

print(xx.ndim)          # 2
x1 = xx.flatten()       # 차원 축소         xx.ravel()
print(x1.ndim)          # 1
y1 = yy

data = np.array([x1, y1])
df = pd.DataFrame(data.T)
df.columns=['x1', 'y1']
print(df.head(3))

model2 = smf.ols(formula="y1~x1", data=df).fit()
print(model2.summary())
print('기울기 : ', model2.params['x1'])
print('절편 : ', model2.params['Intercept'])

# 예측값 확인
new_df = pd.DataFrame({'x1':[-1.70073563, -0.67794537]})
print('예측값 1 : ', model2.predict(new_df))

new_df2 = pd.DataFrame({'x1':[0.1234, 0.2345]})     # 새로운 자료
print('예측값 2 : ', model2.predict(new_df2))
