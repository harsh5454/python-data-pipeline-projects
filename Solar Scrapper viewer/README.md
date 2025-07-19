# 🌌 Solar Scrapper Viewer – ETL Mini Project

This project demonstrates a simple **ETL (Extract, Transform, Load)** pipeline using Python for visualizing planetary data in our Solar System. Instead of live scraping, this version uses a **mock CSV dataset** to ensure stability and offline execution.

---

## 🚀 Objective

- Practice ETL concepts manually without external tools.
- Load and visualize solar system data.
- Generate clean bar charts comparing gravity and moons on planets.

---

## 📁 Folder Structure


Solar Scrapper Viewer/
│
├── scraped_solar_data.csv 
├── Scraped_solar_ETL.py # Main ETL + Visualization script
├── scraped_solar_charts.png # Auto-generated charts (output)
├── README.md # Project documentation


---

## 🔄 ETL Breakdown

### ✅ Extract
- **Source**: `scraped_solar_data.csv`
- Reads planetary mass, diameter, gravity, and moons.

### 🔧 Transform
- Converts all numeric columns to appropriate types.
- Handles formatting like scientific notation.

### 📦 Load & Visualize
- Creates two bar charts:
  - 🌍 Gravity on Planets
  - 🌕 Number of Moons
- Saves as `scraped_solar_charts.png`.

---

## 📊 Sample Output (Chart Preview)

| Planet   | Gravity (m/s²) | Moons |
|----------|----------------|-------|
| Earth    | 9.8            | 1     |
| Jupiter  | 24.8           | 95    |
| Saturn   | 10.4           | 146   |
| Mars     | 3.7            | 2     |
| Neptune  | 11.2           | 14    |
| Mercury  | 3.7            | 0     |

Output chart is auto-generated when you run the script.

---

## 🛠 Technologies Used

- Python 3.x
- Pandas
- Matplotlib

---

## ▶️ How to Run

1. Clone or download the repository.
2. Ensure Python + pip packages installed:
   ```bash
   pip install pandas matplotlib
