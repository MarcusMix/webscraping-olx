import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

file_path = "C:\\Users\\vini6\\OneDrive\\Desktop\\webscraping-olx\\data\\full_rents.json"

rent_data = pd.read_json(file_path)

# transformando price em valor numerico usável
rent_data["price"] = rent_data["price"].str.slice(start=3)
rent_data["price"] = rent_data["price"].str.replace('.', '').astype(float)

# transformando old_price em valor numerico usável
rent_data["old_price"] = rent_data["old_price"].str.slice(start=3)
rent_data["old_price"] = rent_data["old_price"].str.replace('.', '').astype(float)

# dividindo datas
rent_data['date'] = rent_data['date'].astype(str)
rent_data[['date_correct', 'hour']] = rent_data['date'].str.split(' ', expand=True)
rent_data['date_correct'] = pd.to_datetime(rent_data['date_correct'])

# deletando linhas vazias
rent_data.dropna(subset=['title'], inplace=True)


# criar uma conexão com o banco de dados MySQL
engine = create_engine('mysql://root:root@localhost/rents')

sql_table = 'rent_table'

rent_data.to_sql(sql_table, con=engine, if_exists='replace', index=False)

# exportar para XLSX
#rent_data.to_excel("C:\\Users\\vini6\\OneDrive\\Desktop\\webscraping-olx\\data\\transformed_rents.xlsx", index=False)
# rent_data.dtypes