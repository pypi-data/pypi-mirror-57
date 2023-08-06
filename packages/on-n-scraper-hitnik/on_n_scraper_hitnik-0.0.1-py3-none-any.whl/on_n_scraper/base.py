import requests
import os
from requests.exceptions import HTTPError
import datetime
from on_n_scraper.urls import (
    add_path_to_url, add_subdomain_to_url,
    is_url_have_host, url_replace_path
    )
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
from pytz import timezone
import pprint

SECTIONS ={
    'people': 'people',
    'auto': 'auto',
    'tech': 'tech',
    'realt': 'realt',
    }

DOMAIN = 'https://onliner.by/'

class OnlinerNews():

    def __init__(self, section=None):
        self.section = SECTIONS[section]

    @classmethod
    def str_year_month_date_from_date(cls, date):
        year = date.strftime('%Y')
        month = date.strftime('%m')
        day = date.strftime('%d')

        return year, month, day

    def news_urls_list(self, date=None):

        urls = {}
        news_dict = {}
        if not date:
            date = datetime.datetime.now()
        self.year, self.month, self.day = OnlinerNews.str_year_month_date_from_date(date)
        if self.section:
           urls[self.section] = add_path_to_url(add_subdomain_to_url(DOMAIN, self.section), self.year, self.month, self.day)
        else:
            for k, v in SECTIONS.items():
                urls[k] = add_path_to_url(add_subdomain_to_url(DOMAIN, v), self.year, self.month, self.day)
        for sect,url in urls.items():
            r = requests.get(url)
            if r.status_code == 200:
                news_raw_list = self._parse_news_links(r.content)
                for item in news_raw_list:
                    if not is_url_have_host(item['url']):
                        item['url'] = url_replace_path(url, item['url'])
                news_dict[sect] = news_raw_list
            else:
                raise HTTPError(r.status_code)

        return news_dict

    def _get_news_date(self, div_time):
        time_str = re.search(r'\d+:\d+', div_time.text).group()
        news_date = datetime.datetime.strptime(time_str + ' ' + self.day + '.' + self.month + '.' + self.year,
                                               '%H:%M %d.%m.%Y')
        local_tz = timezone('Europe/Minsk')
        news_date = local_tz.localize(news_date)

        return news_date

    def _parse_news_links(self, html):
        news_list = []
        soup = BeautifulSoup(html, 'html.parser')
        news_div = soup.find('div', 'news-tidings__wrapper')
        news_raw_list = news_div.find_all('div', 'news-tidings__item')
        for item in news_raw_list:
            div_time = item.find('div', 'news-tidings__time')
            if not div_time:
                div_time = item.find('div', 'news-tiles__time')
            news_date = self._get_news_date(div_time)
            a = item.find_all('a', href=True)[0]
            url_short = a['href']
            dev_descript = item.find('div', 'news-tidings__speech')
            descript = None
            if dev_descript:
                descript = dev_descript.text.lstrip()
            title = item.find('span', 'news-helpers_show_mobile-small')
            if not title:
                title = item.find('div', 'news-tiles__subtitle')
            title = title.text.lstrip()
            news_list.append({'title': title, 'url': url_short, 'date': news_date, 'description': descript})
        return news_list

    @classmethod
    def get_news_as_str(cls, url):
        r = requests.get(url)
        if r.status_code == 200:
            soup = soup = BeautifulSoup(r.content, 'html.parser')
            text = soup.find('div', 'news-text').get_text().lstrip().split('\n')
            text = filter(None, text)
            text = '\n'.join(text)
            return text
        else:
            raise HTTPError(r.status_code)

    @classmethod
    def get_news_as_file(cls, url, path=None):
        text = OnlinerNews.get_news_as_str(url)
        if not path:
            path = os.getcwd()+os.path.sep+datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'.txt'
        with open(path, 'w') as f:
            f.write(text)
