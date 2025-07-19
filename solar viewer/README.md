# 🪐 Solar System ETL Viewer

## 📌 Overview
This ETL project reads planetary data from a static CSV file, transforms it using `pandas`, and visualizes planetary gravity using `matplotlib`.

## 📂 Files
| File | Description |
|------|-------------|
| `solar_system_data.csv` | Static data file of 8 planets |
| `solar_viewer.py`       | Python ETL and chart generator |
| `planet_gravity.png`    | Bar chart of gravity (auto-generated) |

## 📊 Chart
- Gravity comparison of 8 planets
- Saved as PNG: `planet_gravity.png`

## 🚀 How to Run

```bash
pip install pandas matplotlib
python solar_viewer.py
```