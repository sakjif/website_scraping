import requests
from datetime import date
from datetime import timedelta
from bs4 import BeautifulSoup

today = date.today()
yesterday = today - timedelta(days=1)
parsed_data = []


class Parsing:
    def __init__(self, page_count):
        self.url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page_count}/c37l1700273'
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

    def page_elements(self):
        for elem in self.soup.find_all('div', class_='clearfix'):
            try:
                image = elem.find('picture').find('source').get('data-srcset')
            except AttributeError:
                image = 'Not Found'
            currency = getattr(elem.find('div', class_='price'), 'text', 'Not Found').strip()[0]
            price = getattr(elem.find('div', class_='price'), 'text', 'Not Found').strip()[1::]
            title = getattr(elem.find(class_='title'), 'text', 'Not Found').strip()
            bedroom = getattr(elem.find('span', class_='bedrooms'), 'text', 'Not Found').replace(' ', '').replace('\n', '')
            description = getattr(elem.find(class_='description'), 'text', 'Not Found').replace(' ', '').replace('\n', '')
            location = getattr(elem.find('span', class_=''), 'text', 'Not Found').strip()
            date_posted = getattr(elem.find('span', class_='date-posted'), 'text', 'Not Found').strip().replace('/', '-')
            if '<' in date_posted:
                date_posted = f'{today.strftime("%d-%m-%Y")}'
            elif 'Yesterday' in date_posted:
                date_posted = f'{yesterday.strftime("%d-%m-%Y")}'
            data_tuple = (image, title, location, date_posted, bedroom, description, price, currency)
            parsed_data.append(data_tuple)


for page_count in range(1, 88):
    print(page_count, 'page in parse process')
    parsing = Parsing(page_count)
    parsing.page_elements()
