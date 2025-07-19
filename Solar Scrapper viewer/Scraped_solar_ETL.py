import pandas as pd
import matplotlib.pyplot as plt

# LOAD from fake CSV
df = pd.read_csv("scraped_solar_data.csv")

# Plot charts
plt.figure(figsize=(12, 6))

# Chart 1: Gravity
plt.subplot(1, 2, 1)
plt.bar(df["Planet"], df["Gravity"], color="skyblue")
plt.title("Gravity on Planets")
plt.xlabel("Planet")
plt.ylabel("m/s²")
plt.xticks(rotation=45)

# Chart 2: Moons
plt.subplot(1, 2, 2)
plt.bar(df["Planet"], df["Moons"], color="lightgreen")
plt.title("Number of Moons")
plt.xlabel("Planet")
plt.ylabel("Moons")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("scraped_solar_charts.png")
plt.show()
