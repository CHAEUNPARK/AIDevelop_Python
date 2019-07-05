import pandas as pd
from figure import figure_dot, figure_box, figure_dot_linear,figure_heat
# fixed acidity;"volatile acidity";"citric acid";"residual sugar";"chlorides";"free sulfur dioxide";"total sulfur dioxide";"density";"pH";"sulphates";"alcohol";"quality"

test = []

input_file_red = 'winequality-red.csv'
in_col = ['quality', 'chlorides', 'alcohol', 'fixed acidity', 'residual sugar', 'free sulfur dioxide', 'pH', 'density']


# red wine
wineData_red = pd.read_csv(input_file_red, delimiter=';')     # 12, 5, 11
# col_winData_red = wineData_red[in_col]
col_quality_red = wineData_red[in_col[0]]       # 품질점수
col_chlorides_red = wineData_red[in_col[1]]     # 소금의 양
col_alcohol_red = wineData_red[in_col[2]]       # 알코올 함량
fixed_acidity = wineData_red['fixed acidity']
volatile_acidity = wineData_red['volatile acidity']
citric_acid = wineData_red['citric acid']
residual_sugar = wineData_red['residual sugar']
free_sulfur_dioxide = wineData_red['free sulfur dioxide']
total_sulfur_dioxide = wineData_red['total sulfur dioxide']
density = wineData_red['density']
pH = wineData_red['pH']
sulphates = wineData_red['sulphates']

for i in range(8):
    test.append(wineData_red[in_col[i]])


# series_name = [wineData_red, col_quality_red, col_chlorides_red, col_alcohol_red, fixed_acidity, volatile_acidity,
#                citric_acid, residual_sugar, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates]

# correlation_red
corr_alcohol_red = col_quality_red.corr(col_alcohol_red)
corr_chlorides_red = col_quality_red.corr(col_chlorides_red)
print(corr_alcohol_red, corr_chlorides_red)

# 히트맵
figure_heat(wineData_red)

# 산포도
figure_dot(col_alcohol_red, col_quality_red)

# box plot
figure_box(col_quality_red, col_chlorides_red, col_alcohol_red, pH, density, residual_sugar)

# 대표 직선
figure_dot_linear(col_alcohol_red, col_quality_red)