import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas as pd
import koreanize_matplotlib
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/housing.data', header=None, sep=r'\s+')
df.columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
print(df.head(2))
print(df.corr())    # LSTAT(하층비율), MEDV(집값): -0.737663 음의 상관관계

x = df[['LSTAT']].values
y = df[['MEDV']].values
print(x[:3])
print(y[:3])

# 단항을 통한 선형모델
model = LinearRegression()

# 다항 특성
quad = PolynomialFeatures(degree = 2)
cubic = PolynomialFeatures(degree = 3)

x_quad = quad.fit_transform(x)
x_cubic = cubic.fit_transform(x)
print(x_quad[:3])
print(x_cubic[:3])

# 단순회귀
model.fit(x,y)
x_fit = np.arange(x.min(), x.max(), 1)[:, np.newaxis]
y_lin_fit = model.predict(x_fit)
# print('y_lin_fit : ', y_lin_fit)
model_r2 = r2_score(y,model.predict(x))
print('model_r2 : ', model_r2)          # model_r2 :  0.544146의 설명력을 가지고 있다.

# 2차 
model.fit(x_quad,y)
y_quad_fit = model.predict(quad.fit_transform(x_fit))
q_r2 = r2_score(y,model.predict(x_quad))
print('q_r2 : ', q_r2)                  # q_r2 :  0.640716

# 3차 
model.fit(x_cubic,y)
y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
c_r2 = r2_score(y,model.predict(x_cubic))
print('c_r2 : ', c_r2)                  # c_r2 :  0.6578476

plt.scatter(x,y,label='초기 데이터')
plt.plot(x_fit, y_lin_fit, linestyle=':', label='linear fit(d=1), $R^2=%.2f$'%model_r2, c='b', lw=3)          # R^2를 소수 둘째자리까지 표시
plt.plot(x_fit, y_quad_fit, linestyle='-', label='linear fit(d=2), $R^2=%.2f$'%q_r2, c='r', lw=3)  
plt.plot(x_fit, y_cubic_fit, linestyle='--', label='linear fit(d=3), $R^2=%.2f$'%c_r2, c='k', lw=3)  
plt.xlabel('하위계층 비율')
plt.ylabel('주택가격')
plt.legend()
plt.show()