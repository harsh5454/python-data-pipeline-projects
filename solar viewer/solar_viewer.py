import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("solar_system_data.csv")
df = df.sort_values(by="Gravity (m/s²)", ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(df["Planet"], df["Gravity (m/s²)"], color="orange")
plt.title("Gravity on Planets")
plt.xlabel("Planet")
plt.ylabel("Gravity (m/s²)")
plt.tight_layout()
plt.savefig(r"D:\Data_Project\level_1_manual_etl\solar viewer\planet_gravity.png")
plt.show()
