from bs4 import BeautifulSoup
import requests
import urllib.parse
import webbrowser


def main():
    # Check large version
    URL = "https://raven.cam.ac.uk/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    ravens = soup.find_all("img", class_="raven-logo")
    try:
        assert len(ravens) == 1
        assert ravens[0]["src"] == "/images/raven-logo.gif"
    except AssertionError:
        for raven in ravens:
            webbrowser.open(urllib.parse.urljoin(URL, raven["src"]), new=2)

    # Check small version
    URL2 = "https://raven.cam.ac.uk/auth/login.html"
    page2 = requests.get(URL2)

    soup2 = BeautifulSoup(page2.content, "html.parser")

    ravens2 = soup2.find_all("img", class_="raven-logo")
    try:
        assert len(ravens2) == 2
        assert ravens2[0]["src"] == "/images/raven-logo-small.gif"
        assert ravens2[1]["src"] == "/images/passwordRecovery_sm.png"
    except AssertionError:
        for raven in ravens2:
            webbrowser.open(urllib.parse.urljoin(URL, raven["src"]), new=2)


if __name__ == "__main__":
    main()
