import pandas as pd

excel_file = 'Book2.xlsx'
df = pd.read_excel(excel_file)
json_data = df.to_json(orient='records')
print(json_data)
rev_data = pd.read_json(json_data)
print(rev_data)
