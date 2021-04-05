import requests
from bs4 import BeautifulSoup

LIMIT = 500
URL = f"https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=PYTHON&recruitPage=1&recruitSort=relation&recruitPageCount={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")

    pages = []
    for link in links:
        pages.append(int(link.string))

    last_page = pages[-1]

    return last_page
