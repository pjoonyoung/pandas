import pandas as pd

# food = pd.read_csv('data/food.csv')
# print(food)

acci = pd.read_csv('data/acci.csv', engine='python', encoding='CP949') # 에러 UDF-8
print(acci)