import pandas as pd
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
CCTV_Seoul = pd.read_csv('c:/Users/user/Desktop/cctv_in_seoul.csv', encoding='utf-8')
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
# print(CCTV_Seoul.head())

pop_Seoul = pd.read_excel('c:/Users/user/Desktop/Report.xls', header=2, usecols='B, D, G, J, N', encoding='utf-8')
pop_Seoul.rename(columns={pop_Seoul.columns[0]:'구별'
                          ,pop_Seoul.columns[1]:'인구수'
                          ,pop_Seoul.columns[2]:'한국인'
                          ,pop_Seoul.columns[3]:'외국인'
                          ,pop_Seoul.columns[4]:'고령자'}, inplace=True)
# print(pop_Seoul.head())
#
# print(CCTV_Seoul.sort_values(by='소계', ascending=True).head(5))
# print(CCTV_Seoul.sort_values(by='소계', ascending=False).head(5))

CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년']+ CCTV_Seoul['2015년'] + CCTV_Seoul['2014년'])/CCTV_Seoul['2013년도 이전'] * 100
# print(CCTV_Seoul.sort_values(by='최근증가율',ascending=False).head(5))
pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100
# print(pop_Seoul.head())

data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
# print(data_result.head())
# print(type(data_result))

data_result.set_index('구별', inplace=True)
# print(data_result)
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)

plt.figure()
data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.show()

plt.figure()
data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100
data_result['CCTV비율'].sort_values().plot(kind='barh',
                                         grid=True, figsize=(10,10))
plt.show()

plt.figure(figsize=(6,6))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()