import pandas as pd

data = {'나이': [20, 40, 11, 13],
        '이름': ['홍길동', '이순신', '김유신', '강감찬'],
        '신장': [175.3, 170.5, 180.6, 175.0]

        }

df1 = pd.DataFrame(data)
print(df1['나이']) #특정 열만 출력
print(df1)

li1 = [[1,2],[3,4],[5,6],[13,12],[7,8],[9,6],[5,10]]
df2 = pd.DataFrame(li1, columns=['first','second'])
print(df2)

print(df2.iloc[1])
print(df2.head()) #데이터 값 상위 5개만 가져오기

bools = [False, True, False, True, False, True, False]
print(df2['second'][bools])