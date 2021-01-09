# https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=ai&limit=50
# https://stackoverflow.com/jobs?q=ai

import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=ai&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links:
  pages.append(link.find("span").string)
pages = pages[:-1]
pages = list(map(int, pages))
#https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
max_page = pages[-1]

