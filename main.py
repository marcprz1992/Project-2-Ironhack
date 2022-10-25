from src.cleaning import cleaning_df
from src.visualization import violin
from src.APIWeb import myRequests
from src.APIWeb import superpowers
from src.APIWeb import getLinks

#Import and cleaning
df = cleaning_df("My_code/file_to_analyse.csv")

#API

# Scrapping

# Save dataframe

# Visualizar: generar gráfica + guardas
#gemerar1 y guardar una
dict_ = {
    "Super Powers":"Median number of Comics by main Super Power"
}

n = 0
for key, value in dict_.items():
    n += 1
    violin(df, "comics", key, value, n)   