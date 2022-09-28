from bs4 import BeautifulSoup
import requests
from pathlib import Path

class Piu:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_piu.txt"
        url = "https://piu.org.pl/"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.readline()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        #print(doc.prettify())

        #finding titles and links from html
        announcements = doc.find_all("div", {"id": "main"})
        ogloszenia = announcements[0].find_all("div", {"class": "blogpiu_main_container"})
        for ogloszenie in ogloszenia:
            #print(ogloszenie.prettify())
            title = ogloszenie.find("a")
            title1 = title.find("h4", {"class": "blogpiu_title"}).text
            title2 = title.find("p").text
            title = title1 + " " + title2
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
        new_title = ogloszenia[0].find("a")
        title1 = new_title.find("h4", {"class": "blogpiu_title"}).text
        title2 = new_title.find("p").text
        new_title = title1 + " " + title2

        #writing to file
        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = Piu()
    output = Piu.scrap()
    print(output)