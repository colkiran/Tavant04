
from bs4 import BeautifulSoup

with open("mypage.html", "r") as HFLR:                  # HFRL - file handler
    content = HFLR.read()

    soup = BeautifulSoup(content, 'lxml')

    tag = soup.find("h5")
    print(tag)

    print("-" * 40)

    tag = soup.find("h5").text
    print(tag)

    print("-" * 40)

    crdTitle = soup.findAll('h5')
    print(crdTitle)

    print("-" * 40)

    for ct in crdTitle:
        print(ct.text)

    print("-" * 40)

    cards = soup.findAll("div", class_="card")
    for card in cards:
        crd_title = card.h5.text
        prc = card.a.text.split()[-1]
        # print(prc)
        # print(crd_title)
        print(f"Training on {crd_title} will cost {prc}")
