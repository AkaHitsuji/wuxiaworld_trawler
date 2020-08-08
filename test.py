import requests
from bs4 import BeautifulSoup

url = "https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-1406"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = requests.get(url, headers=HEADERS).text
soup = BeautifulSoup(page, 'html.parser')

chapter_content = soup.find(id="chapter-content")
chapter_content = chapter_content.find_all("p")
# print(chapter_content)
content = ""
for c in chapter_content:
    content += c.text.strip() + "\n\n"

print(content)
# chapter_content = chapter_content.get_text(separator='\n\n')
# chapter_content = chapter_content.replace("Previous Chapter", "").replace("Next Chapter", "")
# chapter_content = chapter_content.lstrip().rstrip()