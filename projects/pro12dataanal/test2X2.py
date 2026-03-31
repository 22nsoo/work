# 교차분석(카이제곱, 카이스퀘어) 가설 검정.
# 변수는 범주형 자료(변수)를 대상으로 교차빈도에 대한 기술 통계량 제공.
# 교차 빈도에 대한 통계적 유의성을 검증해 주는 분석 기법이다.

# 분산이 퍼져 있는 모습을 분포로 만든 것이 카이제곱 분포다.
# 𝙓² = Σ(관측값 - 기대값)²/기대값

# 적합도 : 일원카이제곱 검정
# 독립성, 동질성 검정: 이일원 카이제곱 검정

# 가설을 채택하는 두가지 방법 연습 ------
import pandas as pd

data = pd.read_csv('pass_cross.csv', encoding='euc-kr')
print(data.head())
print(data.shape)       # (50,4)
print(data.shape[0])    # 헹
print(data.shape[1])    # 열
print()
print(data[(data['공부함'] == 1)&(data['합격'] == 1)].shape[0])         # 18
print(data[(data['공부함'] == 1)&(data['불합격'] == 1)].shape[0])       # 7

print('빈도표 작성 -------')
ctab = pd.crosstab(index=data['공부안함'], columns=data['불합격'], margins=True)
ctab.columns = ['합격','불합격','행합']
ctab.index = ['공부함','공부안함','열합']
print(ctab)

# 검정 방법 1 : 카이제곱 표
# 기대 도수 = (각 행의 주변합) * (각 열의 주변합) / 총합<전체 표본수>
# chi = (18-15) ** 2 / 15 + (7-10) ** 2 / 10 +(12-15) ** 2 / 15 + (13-10) ** 2 / 10
print((18-15) ** 2 / 15 + (7-10) ** 2 / 10 +(12-15) ** 2 / 15 + (13-10) ** 2 / 10)      # 3.0

# chi2 = 3.0
# df = 2-1 = 1
# 유의 수준 : 0.05
# 임계값 : 3.84
# 판정 : 카이제곱 검정 통계량 : 3 < 임계값(3.84) 이므로 귀무 채택역 내에 있으므로 귀무가설 채택!
# 그러므로 벼락치기 공부하는 것과 합격여부는 관계가 없다. 는 의견 유지

# 검정방법 2 : p-value 사용
# 95% 신뢰구간 ⍺ = 0.05
import scipy.stats as stats
chi2, p, _, _ = stats.chi2_contingency(ctab)       # 반환값이 4개가 나온다
print(chi2, p)