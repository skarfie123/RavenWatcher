from bs4 import BeautifulSoup
import requests
import urllib.parse
import webbrowser


def main():
    basic_ravens = [
        "/images/raven-logo.gif",
        "/images/raven-logo-small.gif",
        "/images/passwordRecovery_sm.png",
    ]

    check_raven_url("https://raven.cam.ac.uk/", basic_ravens)
    check_raven_url("https://raven.cam.ac.uk/auth/login.html", basic_ravens)


def check_raven_url(arg0, basic_ravens):
    URL = arg0
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    ravens = soup.find_all("img", class_="raven-logo")

    for raven in ravens:
        if raven["src"] not in basic_ravens:
            webbrowser.open(urllib.parse.urljoin(URL, raven["src"]), new=2)


if __name__ == "__main__":
    main()
