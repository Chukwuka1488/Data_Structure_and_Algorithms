import pandas as pd

read_file = pd.read_csv('questions.csv')
pd.set_option('display.max_columns', None)
# print(read_file.head())

read_file.to_excel('question.xlsx', index=None, header=True)
