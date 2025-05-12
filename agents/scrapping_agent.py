from bs4 import BeautifulSoup
import requests

def get_earnings_news():
    url = "https://www.marketwatch.com/latest-news?mod=top_nav"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for tag in soup.select('.article__headline a')[:3]:
        headlines.append(tag.get_text(strip=True))
    return headlines
