# 비선형회귀분석(Non-linear regression)
# : 직선의 회귀선을 곡선으로 변환해 보다 더 정확하게 데이터 변화를 예측하는데 목적이 있다.
# 선형 가정이 어긋날 때(비정규성) 대처할 수 있는 방법으로 다항식 항을 추가한 다음
# # 입력 데이터 특정 변환으로 선형모델을 개선 

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = np.array([1,2,3,4,5])
y = np.array([4,2,1,3,7])

plt.scatter(x,y)
plt.show()
print(np.corrcoef(x,y)[0,1])

