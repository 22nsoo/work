import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars)
print(mtcars.columns)

# Index(['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear','carb']
print(mtcars.info())
# x : hp(마력수), y : mpg(연비)
print(np.corrcoef(mtcars.hp, mtcars.mpg))       # -0.77616837
print(np.corrcoef(mtcars.wt, mtcars.mpg))       # -0.86765938

# 시각화
# plt.scatter(mtcars.hp, mtcars.mpg)
# plt.xlabel('마력수')
# plt.ylabel('연비')
# plt.show()

print('단순 선형회귀')
result = smf.ols(formula='mpg ~ hp', data = mtcars).fit()

print(result.summary())

#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                    mpg   R-squared:                       0.602
# Model:                            OLS   Adj. R-squared:                  0.589
# Method:                 Least Squares   F-statistic:                     45.46
# Date:                Fri, 03 Apr 2026   Prob (F-statistic):           1.79e-07
# Time:                        17:03:52   Log-Likelihood:                -87.619
# No. Observations:                  32   AIC:                             179.2
# Df Residuals:                      30   BIC:                             182.2
# Df Model:                           1                                         
# Covariance Type:            nonrobust                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept     30.0989      1.634     18.421      0.000      26.762      33.436
# hp            -0.0682      0.010     -6.742      0.000      -0.089      -0.048
# ==============================================================================
# Omnibus:                        3.692   Durbin-Watson:                   1.134
# Prob(Omnibus):                  0.158   Jarque-Bera (JB):                2.984
# Skew:                           0.747   Prob(JB):                        0.225
# Kurtosis:                       2.935   Cond. No.                         386.
# ==============================================================================

# yhat = -0.0682*x + 30.0989 + err
print('마력수 110에 대한 연비 예측값 : ', -0.0682*110 + 30.0989 )                                   # 22.5969
print('마력수 110에 대한 연비 예측값 : ', result.predict(pd.DataFrame({'hp':[110]})).values)        # [22.59374995]
# 약간의 오차 발생

print('\n다중선형회귀------------')
result2 = smf.ols(formula='mpg~hp+wt', data = mtcars).fit()
print(result2.summary())
#  37.2273 -0.0318 -3.8778 
print('마력수 110 + 무게 5에 대한 연비 예측 값 : ', (-0.0318*110) + (-3.8778*5) + 37.2273)          # 14.3403
print('마력수 110 + 무게 5에 대한 연비 예측 값 : ', result2.predict(pd.DataFrame({'hp':[110], 'wt':[5]})).values)   # [14.34309224]

print('\n추정치 구하기 --차체 무게를 입력해 연비 추정---')
result3 = smf.ols(formula = 'mpg~wt', data=mtcars).fit()
print(result3.summary())
print('결정계수 : ',result3.rsquared)   # 0.7528327936582646
pred = result3.predict()
print('result3 연비 예측값 : ',pred[:5])

# 새로운 차체 무게로 연비 추정
mtcars.wt = float(input('차체무게 입력 : '))
new_pred = result3.predict(pd.DataFrame(mtcars.wt))
print(f'차체 무게 {mtcars.wt[0]}일 때 예상 연비는{new_pred[0]}')


