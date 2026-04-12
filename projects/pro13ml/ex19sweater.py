# LogisticRegression - 날씨 예보(비가 올지 여부)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/weather.csv')
print(data.head(2), data.shape)             # (366, 12)
data2 = pd.DataFrame()
data2 = data.drop(['Date', 'RainToday'], axis=1)
data2['RainTomorrow'] = data2['RainTomorrow'].map({'Yes':1, 'No':2})
print(data2.head(2), data2.shape)                   # (366, 10)
print(data2['RainTomorrow'].unique())               # [1 0]

# RainTomorrow : 종속변수(범주형, label, class), 나머지열 : 독립변수(feature)

print('데이터 분리 : 학습용(train data), 검증용(test data)')
# 모델의 성능을 객관적으로 파악, 모델 학습과 검증에 사용된 자료가 같다면 오버피팅(과적합) 우려 발생
train, test = train_test_split(data2, test_size=0.3, random_state=42)
print(train.shape, test.shape)
print(train.head(3))