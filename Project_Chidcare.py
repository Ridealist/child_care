##돌봄교실 이용 비율
import pandas as pd
import numpy as np
care = pd.read_csv("C:/Users/Junbo Koh/Downloads/child_care_2019.csv")

#care.head()
#care.dtypes
care2 = care[care['설립구분'] == '공립']
col = np.array([0,6,9,11,12])
care3 = care2.iloc[:,col]

city = care3['시도교육청'].unique()
por = []
for i in city:
    ccity = care3[care3['시도교육청'] == i]
    cpor = ( ccity.sum()[1:,]['오후돌봄참여학생수'] + ccity.sum()[1:,]['방과후학교 연계형돌봄참여학생수'] 
            ) / ( ccity.sum()[1:,]['1-4학년 학생수'] + ccity.sum()[1:,]['5-6학년 학생수'] ) 
    por.append(cpor)

apor = np.array(por)
d = np.column_stack([city, apor])
df = pd.DataFrame(d, columns=('시도교육청', '돌봄이용 비율'))
df.to_excel("C:/Users/Junbo Koh/Downloads/care_2019_portion.xlsx")



##데이터 시각화
#산점도 행렬
import seaborn as sns
import numpy as np

care = pd.read_csv('C:/Users/user/Downloads/care_final_2018.csv' , encoding='cp949')
#care.head()

plt.rcParams['font.family'] = 'Malgun Gothic'
sns.pairplot(care)

#상관계수
r1 = np.corrcoef(care['돌봄참여비'], care['맞벌이가구비율']) ; r1
r2 = np.corrcoef(care['돌봄참여비'], care['기초수급자비율']) ; r2
r3 = np.corrcoef(care['돌봄참여비'], care['사교육참여율']) ; r3


##Linear Regression
import pandas as pd
import statsmodels.api as sm

data2 = pd.read_csv('C:/Users/user/Downloads/final2.csv' , encoding='cp949')
X_cols = ['맞벌이가구비율', '기초수급자비율', '사교육참여율']
X = data2[X_cols]
X = sm.add_constant(X)
Y = data2['돌봄참여비']

model2 = sm.OLS(Y, X)
result2 = model2.fit()
print(result2.summary())


#####

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv('C:/Users/user/Downloads/care_final_2018.csv' , encoding='cp949')
X_cols = ['맞벌이가구비율', '기초수급자비율', '사교육참여율']
X = data[X_cols]
X = sm.add_constant(X)
Y = data['돌봄참여비']

model = sm.OLS(Y, X)
result = model.fit()
print(result.summary())


"""
bg_sl = budget[budget['시도교육청'] == '서울특별시교육청']
#bg_sl.sum()[6:,]
bg_sl.sum()[6:,]['학생복지/교육격차해소'] / bg_sl.sum()[6:,].sum()

bg_ps = budget[budget['시도교육청'] == '부산광역시교육청']
#bg_ps.sum()[6:,]
bg_ps.sum()[6:,]['학생복지/교육격차해소'] / bg_ps.sum()[6:,].sum()
"""