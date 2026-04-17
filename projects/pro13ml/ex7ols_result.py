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

# Covariance Type:            nonrobust                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept      0.7789      0.124      6.273      0.000       0.534       1.023
# 적절성            0.7393      0.038     19.340      0.000       0.664       0.815
# ==============================================================================
# Omnibus:                       11.674   Durbin-Watson:                   2.185
# Prob(Omnibus):                  0.003   Jarque-Bera (JB):               16.003
# Skew:                          -0.328   Prob(JB):                     0.000335
# Kurtosis:                       4.012   Cond. No.                         13.4
# ==============================================================================