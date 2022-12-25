import pandas as pd
import csv

df = pd.read_csv("dwarf_stars.csv")
print(df.shape)

df = df.rename({
    'Star_name': "name",
})