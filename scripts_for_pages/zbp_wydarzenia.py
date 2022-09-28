from bs4 import BeautifulSoup
import requests
from pathlib import Path

class ZbpWydarzenia:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_zbp_wydarzenia.txt"
        url = "https://www.zbp.pl/aktualnosci/biezace-wydarzenia"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.read().strip()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        #print(doc.prettify())

        #finding titles and links from html
        announcements = doc.find("div", {"class": "c-InfoTiles c-InfoTiles--col3"})
        ogloszenia = announcements.find_all("article", {"class": "c-InfoTiles__item"})
        for ogloszenie in ogloszenia:
            title = ogloszenie.find("h3").text.strip()
            if title == last_title:
                end_of_page = 0
                break

            output_string.append(title)
            hrief = ogloszenie.find("a", href=True)

            link = hrief['href']
            if link[0:18] != "https://www.zbp.pl":
                link = "https://www.zbp.pl" + link

            output_string.append(link)

        if end_of_page == 1:
            output_string.append("There are more articles on this page!!!")
            output_string.append("")

        #last title on the web site
        new_title = ogloszenia[0].find("h3").text.strip()

        #writing to file
        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = ZbpWydarzenia()
    output = ZbpWydarzenia.scrap()
    print(output)