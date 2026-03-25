import pandas as pd

# 1. 读取
df = pd.read_csv('1000_books_data.csv')

# 转换成数字 (float)
df['价格'] = df['价格'].str.replace('£', '').str.replace('Â', '').astype(float)

# 算账
print(f" 1000 本书的总价值是: {df['价格'].sum()} 英镑")
print(f" 1000 本书的平均价格是: {df['价格'].mean():.2f} 英镑")
print(f" 全场最贵的书的价格是: {df['价格'].max()} 英镑")

