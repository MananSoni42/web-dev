import os
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as soup
from difflib import SequenceMatcher
import numpy as np

def search_from(lst,name,max_results=10):
    n = min(max_results,len(lst))
    sim = [get_similarity(name,l) for l in lst]
    lst = np.array(lst)
    return list(reversed(lst[np.argsort(sim)][-n:]))

def generate_star_rating(rating):
    rating = round(rating * 2) / 2
    print(rating)
    star_html = ''
    count = 0
    while rating > 0:
        if rating < 1:
            star_html += '<span class="fa fa-star-half-o checked"></span>\n'
        else:
            star_html += '<span class="fa fa-star checked"></span>\n'
        rating -= 1
        count += 1

    while count < 5:
        count += 1
        star_html += '<span class="fa fa-star-o checked"></span>\n'

    return star_html

def get_similarity(s1, s2):
    """
    Measure of how similar str s1 and s2 are.
    Scale from 0 to 1
    """
    t0 = sorted(list(set(s1.split(' ')).intersection(set(s2.split(' ')))))
    t1 = sorted(list(set(t0 + s1.split(' '))))
    t2 = sorted(list(set(t0 + s2.split(' '))))

    r01 = SequenceMatcher(None, t0, t1).ratio()
    r02 = SequenceMatcher(None, t0, t2).ratio()
    r12 = SequenceMatcher(None, t1, t2).ratio()
    return max(r01, r02, r12)

def get_key():
    with open('key') as f:
        key = f.read()
    return key

def get_image_url(isbn):
    key = get_key()
    res = requests.get(f'https://www.goodreads.com/book/isbn/{isbn}.xml?key={key}')
    root = soup(res.text,'xml')
    default_img = 'https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png'
    try:
        small_url = root.book.small_image_url.get_text().strip()
        url = root.book.image_url.get_text().strip()
        if url == '':
            if small_url == '':
                return default_img
            return small_url
    except:
        url = default_img

    return url

def get_book_basic_backup(isbn):
    key = get_key()
    res = requests.get(f'https://www.goodreads.com/book/isbn/{isbn}?key={key}')
    root = soup(res.text,'xml')
    try:
        try:
            title = root.book.title.get_text()
        except:
            title = ''
        try:
            year = root.book.publication_year.get_text()
        except:
            year = ''
        try:
            author = root.book.authors.author.find('name').get_text()
        except:
            author = ''
    except:
        title = ''
        author = ''
        year = ''
    return title, author, year
def get_book_info(isbn):
    key = get_key()
    res = requests.get(f'https://www.goodreads.com/book/isbn/{isbn}?key={key}')
    root = soup(res.text,'xml')
    try:
        desc = root.book.description.get_text()
        try:
            root1 = soup(desc,'lxml')
            short_desc = root1.blockquote.get_text()
        except:
            short_desc = ''
    except:
        short_desc = ''
        desc = ''
    return short_desc, desc

def get_rating_info(isbn):
    key = get_key()
    res1 = requests.get(f'https://www.goodreads.com/book/review_counts.json?isbns={isbn}&key={key}')
    res2 = requests.get(f'https://www.goodreads.com/book/isbn/{isbn}?key={key}')
    root = soup(res2.text,'xml')

    try:
        avg_rating = float(res1.json()["books"][0]["average_rating"])
    except:
        avg_rating = 0
    try:
        rating_dist = root.book.rating_dist.get_text().split('|')
        rating_dist = [int(r.split(':')[1]) for r in rating_dist]
    except:
        rating_dist = [0, 0, 0, 0, 0, 0]
    return avg_rating, rating_dist

def search_books(title):
    pass
