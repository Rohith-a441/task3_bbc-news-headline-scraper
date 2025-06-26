import requests
from bs4 import BeautifulSoup

# URL of the news website to scrape
URL = "https://www.bbc.com/news"

# Sending a GET request to fetch the HTML content of the page
response = requests.get(URL)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Finding all the headline tags (BBC uses <h2> tags for top stories)
    headlines = soup.find_all("h2")

    # Extracting text content and removing duplicates using set
    unique_headlines = list(set([headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]))

    # Saving  headlines to a text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for idx, title in enumerate(unique_headlines, 1):
            file.write(f"{idx}. {title}\n")

    print("✅ Headlines successfully scraped and saved to 'headlines.txt'!")
else:
    print(f"❌ Failed to retrieve page. Status code: {response.status_code}")
