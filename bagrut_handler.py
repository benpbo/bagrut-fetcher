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
    sub_terms = soup.body.find_all('li', 'single-sub-term')
    sub_term = [sub_term for sub_term in sub_terms if date in sub_term.find('h3').text][0]
    pdf_items = sub_term.find_all('li', 'pdf-item')
    bagrut_pdfs = [pdf_item.find_all('a', 'black-btn') for pdf_item in pdf_items if pdf_item.find('div', 'pdf-info').find('span', 'first-line').text == str(bagrut_id)][0]
    for bagrut_pdf in bagrut_pdfs:
        print(bagrut_pdf['href'])

