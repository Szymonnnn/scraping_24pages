from bs4 import BeautifulSoup
import requests
from pathlib import Path

class NbpKomunikaty:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_nbp_komunikaty.txt"
        url = "https://www.nbp.pl/home.aspx?f=/komunikaty/index.html"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.read().strip()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        #print(doc.prettify())

        #finding titles and links from html
        announcements = doc.find("table", {"class": "newscols"})
        ogloszenia = announcements.find_all("td", {"class": "box_text"})
        for ogloszenie in ogloszenia:
            title = ogloszenie.find("a").text.strip()
            if title == last_title:
                end_of_page = 0
                break

            output_string.append(title)
            hrief = ogloszenie.find("a", href=True)

            link = hrief['href']
            if link[0:18] != "https://www.nbp.pl":
                link = "https://www.nbp.pl" + link

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
    obj = NbpKomunikaty()
    output = NbpKomunikaty.scrap()
    print(output)