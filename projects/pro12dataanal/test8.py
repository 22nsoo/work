# *단일 모집단의 평균에 대한 가설검정(one samples t test)
# 실습 예제 1
# A 중학교 1 학년 1 반 학생들의 실험 결과가 담긴 파일을 읽어 처리
# 국어 점수 평균 검정(80) student csv

# 귀무 : 학생들의 국어점수 평균은 80이다.
# 대립 : 학생들의 국어점수 평균은 80이 아니다.

import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/student.csv')
print(data.head())
print(data.describe())
