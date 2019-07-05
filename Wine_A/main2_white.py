import pandas as pd
from figure import figure_dot, figure_box, figure_dot_linear, figure_heat

input_file_white = 'winequality-white.csv'
in_col = ['quality', 'chlorides', 'alcohol']

# white wine
wineData_white = pd.read_csv(input_file_white, delimiter=';')     # 12, 5, 11
# col_winData_white = wineData[in_col]
col_quality_white = wineData_white[in_col[0]]       # 품질점수
col_chlorides_white = wineData_white[in_col[1]]     # 소금의 양
col_alcohol_white = wineData_white[in_col[2]]       # 알코올 함량

# correlation_white
corr_alcohol_white = col_quality_white.corr(col_alcohol_white)
corr_chlorides_white = col_quality_white.corr(col_chlorides_white)
print(corr_alcohol_white, corr_chlorides_white)

# 히트맵
figure_heat(wineData_white)

# 산포도
figure_dot(col_alcohol_white, col_quality_white)
figure_dot(col_chlorides_white, col_quality_white)

# 박스 플롯
figure_box(col_quality_white, col_chlorides_white, col_alcohol_white)

# 대표 직선
figure_dot_linear(col_alcohol_white, col_quality_white)


