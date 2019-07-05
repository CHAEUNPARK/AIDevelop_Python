import pandas as pd
from figure import figure_dot, figure_box, figure_dot_linear, figure_heat

input_file_white = 'winequality-white.csv'
in_col = ['quality', 'chlorides', 'alcohol', 'fixed_acidity', 'volatile_acidity',
          'citric_acid', 'residual_sugar', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
          'pH', 'sulphates']

ingred = []
corr = []

# series_name = [wineData_red, col_quality_red, col_chlorides_red, col_alcohol_red, fixed_acidity, volatile_acidity,
#                citric_acid, residual_sugar, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates]

# white wine
wineData_white = pd.read_csv(input_file_white, delimiter=';')     # 12, 5, 11

for i in range(12):
    ingred.append(wineData_white[in_col[i]])



# 히트맵
figure_heat(wineData_white)

# 산포도
figure_dot(ingred[2], ingred[0])
figure_dot(ingred[1], ingred[0])

# 박스 플롯
figure_box(col_quality_white, col_chlorides_white, col_alcohol_white)

# 대표 직선
figure_dot_linear(col_alcohol_white, col_quality_white)


