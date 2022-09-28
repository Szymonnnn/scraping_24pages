from bs4 import BeautifulSoup
import requests
from pathlib import Path

class PiuAktualnosci:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_piu_aktualnosci.txt"
        url = "https://piu.org.pl/aktualnosci/"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.readline()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        #print(doc.prettify())

        #finding titles and links from html
        announcements = doc.find("article", {"id": "post-769"})
        ogloszenia = announcements.find_all("div", {"class": "wrap clearfix"})
        for ogloszenie in ogloszenia:
            #print(ogloszenie.prettify())
            title = ogloszenie.find("div", {"class": "title"}).text[1:-1]
            if title == last_title:
                end_of_page = 0
                break

            output_string.append(title)
            hrief = ogloszenie.find("a", href=True)

            link = hrief['href']
            output_string.append(link)

        if end_of_page == 1:
            output_string.append("There are more articles on this page!!!")
            output_string.append("")

        #last title on the web site
        new_title = ogloszenia[0].find("div", {"class": "title"}).text[1:-1]
        #writing to file
        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = PiuAktualnosci()
    output = PiuAktualnosci.scrap()
    print(output)