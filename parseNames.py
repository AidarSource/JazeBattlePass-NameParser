from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup

# save all the nicknames to 'CSV' file format
filename = "BattlePassNicknames.csv"
f = open(filename, "a", encoding="utf-8")
headers1 = "Member of JAZE Battle Pass 2019\n"
f.write(headers1)
# start page
names = []
i = 1
while True:
    # disable jaze guard. turn off html 'mod_security'
    link = 'https://jaze.ru/forum/topic?id=50&page='+str(i)
    my_url = Request(
        link,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    i += 1  # increment page no for next run
    uClient = uReq(my_url)
    if uClient.url != link:
        break
    page_html = uClient.read()
    # Check if there was a redirect
    uClient.close()
    # html parsing
    page_soup = soup(page_html, "html.parser")
    # grabs each name of player
    containers = page_soup.findAll("div", {"class": "top-area"})

    for container in containers:
        playerName = container.div.a.text.strip()
        if playerName not in names:
            names.append(playerName)

for name in names:
    f.write(name + "\n")
f.close()
