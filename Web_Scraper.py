from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

#Get webpage function
#Makes HTTP get request to the url specified as a param
def get_page(url):
    