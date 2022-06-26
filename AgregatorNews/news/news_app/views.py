from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


hack = 'https://thehackernews.com/'
secnews= 'https://www.itnews.com.au/technology/security'
inf = 'https://www.infosecurity-magazine.com/news/'


hn_list=[]
secnews_list = []
inf_list = []

def get_hack():
    r = requests.get(hack).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('div', class_='body-post clear')

    for post in posts:
        title = post.find('h2', class_='home-title').text
        url = post.find('a').get('href')
        data = {
            'title':title,
            'url': url
        }
        hn_list.append(data)

def get_secnews():
    r = requests.get(secnews).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('div', class_='small-6 medium-4 columns featured-article-wrapper')

    for post in posts:
        title = post.find('h2', class_='featured-article-heading').text
        url = post.find('a').get('href')
        url = 'https://www.itnews.com.au' + url
        data = {
            'title': title,
            'url': url
        }
        secnews_list.append(data)


def get_inf():
    r = requests.get(inf).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('div', class_='webpage-item with-thumbnail')

    for post in posts:
        title = post.find('h3').get_text()
        url = post.find('a').get('href')
        data ={
            'title': title,
            'url': url
        }
        inf_list.append(data)


get_hack()
get_secnews()
get_inf()


def home(requests):
    context = {
        'hn_list': hn_list,
        'secnews_list': secnews_list,
        'inf_list': inf_list
    }
    return render(requests, 'news_app/home.html', context)

