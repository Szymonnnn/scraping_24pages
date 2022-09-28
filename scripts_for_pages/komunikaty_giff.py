from bs4 import BeautifulSoup
import requests
from pathlib import Path

class KomunikatyGiff:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_komunikaty_giff.txt"
        url = "https://www.gov.pl/web/finanse/komunikaty-giif"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.readline()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        #finding titles and links from html
        announcements = doc.find_all("div", {"class": "art-prev"})
        ogloszenia = announcements[0].find_all("li")
        for ogloszenie in ogloszenia:
            title = ogloszenie.find("div", {"class": "title"})
            title = title.string
            if title == last_title:
                end_of_page = 0
                break

            output_string.append(title)
            hrief = ogloszenie.find("a", href=True)

            link = "https://www.gov.pl" + hrief['href']
            output_string.append(link)

        if end_of_page == 1:
            output_string.append("There are more articles on this page!!!")
            output_string.append("")

        #last title on the web site
        new_title = ogloszenia[0].find("div", {"class": "title"}).string

        #writing to file
        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = KomunikatyGiff()
    output = KomunikatyGiff.scrap()
    print(output)