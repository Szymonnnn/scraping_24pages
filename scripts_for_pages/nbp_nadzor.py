from bs4 import BeautifulSoup
import requests
from pathlib import Path

class NbpNadzor:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_nbp_nadzor.txt"
        url = "https://www.nbp.pl/nadzormakroostroznosciowy/index.aspx"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.read().strip()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        #print(doc.prettify())

        #finding titles and links from html
        announcements = doc.find("ul", {"class": "nb hilines"})
        ogloszenia = announcements.find_all("li")
        for ogloszenie in ogloszenia:
            titles = ogloszenie.find_all("div")
            title = titles[1].text.strip()[0:-9]
            if title == last_title:
                end_of_page = 0
                break

            output_string.append(title)
            hrief = titles[1].find("a", href=True)

            link = hrief['href']
            if link[0:18] != "https://www.nbp.pl":
                link = "https://www.nbp.pl" + link

            output_string.append(link)

        if end_of_page == 1:
            output_string.append("There are more articles on this page!!!")
            output_string.append("")

        #last title on the web site
        new_titl = ogloszenia[0].find_all("div")
        new_title = new_titl[1].text.strip()[0:-9]

        #writing to file
        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = NbpNadzor()
    output = NbpNadzor.scrap()
    print(output)