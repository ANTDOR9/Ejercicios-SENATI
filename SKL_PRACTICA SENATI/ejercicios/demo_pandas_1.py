import pandas as pd
from sqlalchemy import create_engine
user='postgres'
password='123'
host='10.0.222.18'
port='5432'
database='tallerdb'
engine= create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
sql="select * from familia"
familia= pd.read_sql(sql, engine)
print (familia)

sql="select * from categoria"
categoria= pd.read_sql(sql, engine)
print (categoria)

vista_categorias = categoria.merge(familia, how='inner', on='idfamilia')
vista_categorias = vista_categorias.rename(columns={'nombre_x':'categoria','nombre_y':'familia'})
print(vista_categorias)

vista_resumen_categorias= vista_categorias[['categoria','familia']]
print(vista_resumen_categorias)

print(vista_resumen_categorias.groupby('familia')['categoria'].count())