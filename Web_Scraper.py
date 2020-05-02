from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

#Get webpage function
#Makes HTTP get request to the url specified as a param
def get_page(url):
    try:
        with closing(get(url, stream=True)) as response:
            if good_response(response):
                return response.content
            else:
                return None
    except RequestException as e:
        print("Error during request to webpage.")
        return None

#Checks to see if the webpage response is valid and that the request worked
def good_response(response):
    content_type = response.headers["Content-Type"].lower()
    return(response.status_code == 200 and content_type is not None and content_type.find("html") > -1)
    
#Main function
def main():
    raw_html = get_page("http://www.fabpedigree.com/james/mathmen.htm")
    print(len(raw_html))

#Call main function
if __name__ == "__main__":
    main()