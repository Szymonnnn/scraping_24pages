from bs4 import BeautifulSoup
import requests
from pathlib import Path

class RfSaduNajwyzszego:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_rf_sadu_najwyzszego.txt"
        url = "https://rf.gov.pl/o-nas/wnioski-o-uchwale-sadu-najwyzszego/"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.readline()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        #print(doc.prettify())

        #finding titles and links from html
        announcements = doc.find("article", {"id": "post-4034"})
        ogloszenia = announcements.find_all("p")

        new_title = ""
        i = 0
        while i < len(ogloszenia):
            title = ogloszenia[i].find("strong")

            if end_of_page == 0:
                break

            if title:
                title = title.text
                if title == last_title:
                    end_of_page = 0
                    if not new_title:
                        new_title = title
                    break

                if not new_title:
                        new_title = title

                output_string.append(title)
                #print(title)
                i += 1

                hrief = ogloszenia[i].find("a", href=True)
                if hrief:
                    link = hrief['href']
                    output_string.append(link)
                    i += 1
                    hrief = ogloszenia[i].find("a", href=True)
                    if hrief:
                        link = hrief['href']
                        output_string.append(link)
                        i += 1
                    else:
                        output_string.append("")
                        i += 1
                else:
                    output_string.append("")
                    output_string.append("")
                    i += 1

            else:
                i+=1

        if end_of_page == 1:
            output_string.append("There are more articles on this page!!!")
            output_string.append("")
            output_string.append("")

        #print(new_title)
        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = RfSaduNajwyzszego()
    output = RfSaduNajwyzszego.scrap()
    print(output)