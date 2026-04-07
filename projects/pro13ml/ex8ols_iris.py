# 단순선형회귀 - iris dataset
# 상관관계가 약한 경우와 강한 경우로 회귀분석모델을 생성 후 비교

import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head(3), type(iris))
print(iris.iloc[:, 0:4].corr())

#               sepal_length  sepal_width  petal_length  petal_width
# sepal_length      1.000000    -0.117570      0.871754     0.817941
# sepal_width      -0.117570     1.000000     -0.428440    -0.366126        반비례 관계
# petal_length      0.871754    -0.428440      1.000000     0.962865
# petal_width       0.817941    -0.366126      0.962865     1.000000        정비례 관계

print('\n연습1 : 상관관계가 약한 변수를 사용  -0.117570')
result1 = smf.ols(formula='sepal_length~sepal_width', data=iris).fit()
print(result1.summary())
print('R squared : ', result1.rsquared)             # 0.013822654141080748
print('p-value : ', result1.pvalues.iloc[1])        # 0.15189826071144846

# 시각화
plt.scatter(iris.sepal_width, iris.sepal_length)
plt.plot(iris.sepal_width, result1.predict(), color='r')
plt.show()


print('\n연습2 : 상관관계가 강한 변수 사용')
result2 = smf.ols(formula='sepal_length~petal_length', data=iris).fit()         # 독립변수 sepal_length, 종속변수 petal_length 
print(result2.summary())
print('R squared : ', result2.rsquared)             # 0.7599546457725151
print('p-value : ', result2.pvalues.iloc[1])        # 1.0386674194498421e-47 < 0.05 이 모델은 유의한 모델

# 시각화
plt.scatter(iris.petal_length, iris.sepal_length)
plt.plot(iris.petal_length, result2.predict(), color='b')
plt.show()

# 새로운 값으로 예측
print('실제값 : ', iris.sepal_length[:10].values)       # 76 퍼센트의 확률로 예측한 결과값 
print('예측값 : ', result2.predict()[:10])
print()

new_data = pd.DataFrame({'petal_length' : [1.1,0.5,6.0]})
y_pred = result2.predict(new_data)
print('예측 결과 : ', y_pred.values)

# 설명력이 좋은 모델을 만들려면 상관계수를 먼저 봐야 한다.
# 산점도를 항상 그려야 한다.
print('\n연습2 : 독립변수를 복수로 사용 - 다중선형회귀')
result3 = smf.ols(formula='sepal_length ~ petal_length + petal_width', data = iris).fit()
column_select = '+'.join(iris.columns.difference(['sepal_length', 'sepal_width', 'species']))
print(column_select)
result3 = smf.ols(formula='sepal_length ~' + column_select, data=iris).fit()
print(result3.summary())

# 연습2 : 독립변수를 복수로 사용 - 다중선형회귀
# petal_length+petal_width
#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:           sepal_length   R-squared:                       0.766
# Model:                            OLS   Adj. R-squared:                  0.763
# Method:                 Least Squares   F-statistic:                     241.0
# Date:                Fri, 03 Apr 2026   Prob (F-statistic):           4.00e-47
# Time:                        16:50:29   Log-Likelihood:                -75.023
# No. Observations:                 150   AIC:                             156.0
# Df Residuals:                     147   BIC:                             165.1
# Df Model:                           2                                         
# Covariance Type:            nonrobust                                         
# ================================================================================
#                    coef    std err          t      P>|t|      [0.025      0.975]
# --------------------------------------------------------------------------------
# Intercept        4.1906      0.097     43.181      0.000       3.999       4.382
# petal_length     0.5418      0.069      7.820      0.000       0.405       0.679
# petal_width     -0.3196      0.160     -1.992      0.048      -0.637      -0.002
# ==============================================================================
# Omnibus:                        0.383   Durbin-Watson:                   1.826
# Prob(Omnibus):                  0.826   Jarque-Bera (JB):                0.540
# Skew:                           0.060   Prob(JB):                        0.763
# Kurtosis:                       2.732   Cond. No.                         25.3
# ==============================================================================
