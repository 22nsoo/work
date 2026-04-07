# 단순선형회귀 : ols의 Regression Results의 이해
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinking_water.csv')
print(df.head(3))
print(df.corr())

model = smf.ols(formula='만족도~적절성', data = df).fit()
print(model.summary())
print('parameters : ', model.params)
print('R-squared : ', model.rsquared)       # 0.5880630629464405
print('p-value : ', model.pvalues)          # 1.454388e-09
print('예측값 : ', model.predict()[:5])
print('실제값 : ', df.만족도[:5].values)
# 예측값 :  [3.73596305 2.99668687 3.73596305 2.25741069 2.25741069]
# 실제값 :  [3 2 4 2 2]

plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도, 1)
plt.plot(df.적절성, slope*df.적절성 + intercept, c = 'b')
plt.show()