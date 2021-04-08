import requests
from bs4 import BeautifulSoup

URL_1 = f"https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=PYTHON&recruitPage="
URL_2 = f"&recruitSort=relation&recruitPageCount=500"


def get_last_page():
    result = requests.get(URL_1 + URL_2)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")

    pages = []
    for link in links:
        pages.append(int(link.string))
    last_page = pages[-1]

    return last_page


def extract_job(html):
    title = html.find("div", {"class": "area_corp"}
                      ).find("strong").find("span")
    print(title)


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL_1}{page+1}{URL_2}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("h2", {"class": "job_tit"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
