from bs4 import BeautifulSoup
import requests
from pathlib import Path

class NbpPublikacje:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_nbp_publikacje.txt"
        url = "https://www.nbp.pl/nadzormakroostroznosciowy/publikacje.aspx"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.readline()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        #finding titles and links from html
        announcements = doc.find("div", {"id": "publikacje"})
        ogloszenia = announcements.find_all("ul")
        for ogloszenie in ogloszenia:
            title = ogloszenie.find("a")
            title = title.text
            if title == last_title:
                end_of_page = 0
                break

            output_string.append(title)
            hrief = ogloszenie.find("a", href=True)

            link = "https://www.nbp.pl" + hrief['href']
            output_string.append(link)

        if end_of_page == 1:
            output_string.append("There are more articles on this page!!!")
            output_string.append("")

        #last title on the web site
        new_title = ogloszenia[0].find("a").text

        #writing to file
        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = NbpPublikacje()
    output = NbpPublikacje.scrap()
    print(output)