import pandas as pd
import numpy as np

df = pd.read_csv(r"c:\Users\izhan\OneDrive\Desktop\Sample - Superstore.csv", encoding='latin1')

print(df.head())

print(df.info())

df.drop(columns=['Row ID'], inplace=True)
print(df.info())

df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print(df.duplicated().sum())

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

df["Profit Margin"] = df["Profit"] / df["Sales"]

df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days
avg_shipping = df.groupby("Ship Mode")["Shipping Days"].mean()
print(avg_shipping)
print(df.head(10))


region_sales = df.groupby("Region")["Sales"].sum()
print("Region Sales:")
print(region_sales)

region_sales_sorted = region_sales.sort_values(ascending= False)
print("Decending Region Sales:")
print(region_sales_sorted)

top_region = region_sales.idxmax()
print("Highest Sales Region:")
print(top_region)

region_profit = df.groupby("Region")["Profit"].sum()
print("Region Profit:")
print(region_profit)

top_profit_region = region_profit.idxmax()
print("highest Region Profit:")
print(top_profit_region)

print(df[["Category","Sub-Category"]].head(15))

profit_by_category = df.groupby(["Category","Sub-Category"])["Profit"].sum()
print("Profit by catergory:")
print(profit_by_category)

sorted_category = profit_by_category.sort_values(ascending= False)
print("Dec Profit of each sub category:")
print(sorted_category)

get_money = profit_by_category.idxmax()
print("Sub category get more profit:")
print(get_money)

lose_money = profit_by_category.idxmin()
print("Sub category get less profit:")
print(lose_money)


highest_sc = ((df.groupby("Customer Name")["Sales"].sum()).sort_values(ascending=False)).head(10)
print("Top 10 highest sales customer:")
print(highest_sc)

yearly_sales = df.groupby("Year")["Sales"].sum()
print("Yerly sale")
print(yearly_sales)

strongest_month = df.groupby(["Year","Month"])["Sales"].sum()
print("Strongest month:")
print(strongest_month.idxmax())

product_sales = (df.groupby("Product Name")["Sales"]).sum().sort_values(ascending=False)
print(product_sales.head(10))

product_profit = (df.groupby("Product Name")["Profit"]).sum().sort_values(ascending=False)
print(product_profit[product_profit < 0])

no_discount_profit = df[df["Discount"] == 0]["Profit"].mean()
heavy_discount_profit = df[df["Discount"] >= 0.5]["Profit"].mean()

print("No discount avg profit:", no_discount_profit)
print("Heavy discount (50%+) avg profit:", heavy_discount_profit)