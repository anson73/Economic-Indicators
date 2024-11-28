import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_aus_data():
    """
    Get economic data for Australia
    """
    ssl._create_default_https_context = ssl._create_unverified_context

    rba = "https://www.rba.gov.au/"
    abs = "https://www.abs.gov.au/"

    url = rba
    page = urlopen(url)

    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print(soup.get_text().replace("\n", " "))

if __name__ == "__main__":
    get_aus_data()
