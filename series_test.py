import pandas as pd

se1 = pd.Series([50,20,10,40], index = ['홍길동','이순신','김유신','강감찬'])
print(se1)
print("")
print(se1[['이순신','홍길동']])
print("")
print(se1.values)
print(se1.index)
print(sorted(se1.values))
print(sorted(se1.index))
print("------------------------------------------")
list1 = [4,21,5,3,48,5,32,75,5,9,8,5,5,7,1,1,2,]
se2 = pd.Series(list1) # list 를 Series로 변환
se2_unique = pd.unique(se2)
print(se2_unique)
print("------------------------------------------")
age = {'홍길동':23,'이순신':30,'김유신':40,'강감찬':31}
se3 = pd.Series(age)
print(se3)
