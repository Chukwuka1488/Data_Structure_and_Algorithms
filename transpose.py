import pandas as pd

df = pd.read_csv("/Users/haykay14/Downloads/my_file_100.csv")

print(df.head())

x = df.to_dict()
print(x)