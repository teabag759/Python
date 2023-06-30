# PyPi(https://pypi.org/)
    # python package 소개 사이트

# beautifulsoup : 웹페이지에서 필요한 정보를 scrap 할 수 있는 library
    # terminal에서 "pip install beautifulsoup4" 입력

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
