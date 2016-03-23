import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def get_pkg_updates(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    return soup.find(id="pkg-updates")

def print_table(headers, data):
    print(tabulate(data, headers=headers))
