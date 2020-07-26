from requests import get
from datetime import datetime
from bs4 import BeautifulSoup
import re


class Bagrut:
    def __init__(self, link: str, is_solution: bool = False):
        self.link = link
        self.is_solution = is_solution


def get_bagrut(date: str, subject: str, semester: str, bagrut_id: int, year: int = 0) -> Bagrut:
    base_url = 'https://www.geva.co.il/solution_term'
    regex = '\d+[/.-]\d+[/.-](\d+)'
    year = re.findall(regex, date)
    url = base_url + f'/{subject}_{year[0]}_{semester}'
    print(url)
    res = get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    terms = soup.body.find('ul', attrs={'class': 'sub-terms'})
    single_sub_terms = terms.find_all('li', attrs={'class': 'single-sub-term'})

    print(type(terms))
    print(type(single_sub_terms))
