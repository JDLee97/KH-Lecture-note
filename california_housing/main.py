from sklearn.datasets import fetch_california_housing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = fetch_california_housing()
X = data.data
y = data.target
df = pd.DataFrame(data = X, columns = data.feature_names)
df['Price'] = y

# 데이터 저장
df.to_csv("housing_data.csv",index=False)

print(df.info())
print(df.columns)
# print(df.shape)
# print(df.describe())

# 칼럼별 결측치
print(df.isna().sum())

# 데이터 탐색 - histplot
plt.figure(figsize = (10,10))
# cor = df.corr()
# sns.heatmap(data = cor, cmap = "coolwarm",annot = True)
sns.histplot(data = df , x = 'Price', bins = 30, kde = True)
plt.show()

