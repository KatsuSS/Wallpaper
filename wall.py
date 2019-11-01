import click
import datetime
import calendar

import requests
from bs4 import BeautifulSoup
import re


def make_url(month, year):
    url = 'https://www.smashingmagazine.com/{}/{:02d}/desktop-wallpaper-calendars-{}-{}/'
    new_year = year
    new_month = month - 1
    month_name = calendar.month_name[month].lower()

    if month == 1:
        new_month = 12
        new_year = year - 1

    url = url.format(new_year, new_month, month_name, year)
    return url


def session(ses, url):
    try:
        request = ses.get(url)
        return request
    except requests.exceptions.RequestException as e:
        print(e)


def create_file(link, ses):
    filename = link.split('/')[-1]
    img = session(ses, link)
    img = img.content
    try:
        with open(filename, 'wb') as output_file:
            output_file.write(img)
    except IOError as e:
        print(e)


@click.command()
@click.option('-m', '--month', default=datetime.datetime.now().month, help='Default current month', type=int)
@click.option('-y', '--year', default=datetime.datetime.now().year, help='Default current year', type=int)
@click.option('-c', '--cal', default='cal', help='Default with calendar(cal), else (nocal)')
@click.option('-s', '--size', default='1920x1080', help='Size-format "(width)x(height)"')
def main(month, year, cal, size):

    url = make_url(month, year)
    ses = requests.Session()
    request = session(ses, url)

    soup = BeautifulSoup(request.text, 'lxml')
    if cal == 'cal':
        str_pat = 'http:\/\/files\..*?\/cal\/..*?{}\..*'.format(size)
    else:
        str_pat = 'http:\/\/files\..*?\/nocal\/..*?{}\..*'.format(size)
    pattern = re.compile(str_pat)
    links = [a['href'] for a in soup.find_all('a', href=pattern)]

    for link in links:
        create_file(link, ses)


if __name__ == "__main__":
    main()
