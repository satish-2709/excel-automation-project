import pandas as pd

df = pd.read_excel("sales_data.xlsx")

total_sales = df["Sales"].sum()
df["Percentage"] = (df["Sales"] / total_sales) * 100

df.to_excel("sales_report.xlsx", index=False)

print("Report generated successfully!")