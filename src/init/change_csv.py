import pandas as pd

df = pd.read_excel("data/raw/Online Retail.xlsx")
df.to_csv("data/processed/online_retail.csv", index=False, encoding="utf-8-sig")