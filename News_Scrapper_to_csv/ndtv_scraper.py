import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Target NDTV Latest News URL
URL = "https://www.ndtv.com/latest"
response = requests.get(URL)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find headlines
# Headlines are within divs with class 'news_Itm' and inside <h2> tags
headlines = soup.find_all("div", class_="news_Itm")

news_data = []

for idx, item in enumerate(headlines, start=1):
    title_tag = item.find("h2")
    if title_tag and title_tag.a:
        news_data.append({
            "Rank": idx,
            "Title": title_tag.text.strip(),
            "Link": title_tag.a['href']
        })

# Step 4: Convert to DataFrame and Save
df = pd.DataFrame(news_data)
df.to_csv("ndtv_headlines.csv", index=False)
print("✅ NDTV headlines saved to ndtv_headlines.csv")
