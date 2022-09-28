from bs4 import BeautifulSoup
import requests
from pathlib import Path

class KnfAktualnosci:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_knf_aktualnosci.txt"
        url = "https://www.knf.gov.pl/aktualnosci"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.read().strip()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        #print(doc.prettify())

        #finding titles and links from html
        announcements = doc.find("ul", {"class": "col-lg-12 excerpts"})
        ogloszenia = announcements.find_all("div", {"class": "news-item-desc"})
        for ogloszenie in ogloszenia:
            title = ogloszenie.find("a").text.strip()
            if title == last_title:
                end_of_page = 0
                break

            output_string.append(title)
            hrief = ogloszenie.find("a", href=True)

            link = hrief['href']
            if link[0:22] != "https://www.knf.gov.pl":
                link = "https://www.knf.gov.pl" + link

            output_string.append(link)

        if end_of_page == 1:
            output_string.append("There are more articles on this page!!!")
            output_string.append("")

        #last title on the web site
        new_title = ogloszenia[0].find("a").string.strip()

        #writing to file
        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = KnfAktualnosci()
    output = KnfAktualnosci.scrap()
    print(output)