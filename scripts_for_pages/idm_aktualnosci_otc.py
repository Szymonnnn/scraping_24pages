from bs4 import BeautifulSoup
import requests
from pathlib import Path

class IdmAktualnosciOtc:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_idm_aktualnosci_otc.txt"
        url = "https://idm.com.pl/pl/idm-dla-rynkow-otc/aktualnosci-otc"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.readline()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        #print(doc.prettify())

        #finding titles and links from html
        announcements = doc.find("div", {"class": "items-leading"})
        ogloszenia = announcements.find_all("h2")
        kol_akapit = 0
        for ogloszenie in ogloszenia:
            title = ogloszenie.text[1:-1]
            if title == last_title:
                end_of_page = 0
                break

            output_string.append(title)
            
            akapit = announcements.find("div", {"class": "leading-" + str(kol_akapit)})

            kol_akapit += 1
            hrief = akapit.find("a", href=True)

            link = hrief['href']
            if link[:18] != "https://idm.com.pl":
                link = "https://idm.com.pl" + link
            output_string.append(link)

        if end_of_page == 1:
            output_string.append("There are more articles on this page!!!")
            output_string.append("")

        #last title on the web site
        new_title = ogloszenia[0].text[1:-1]
        #writing to file
        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = IdmAktualnosciOtc()
    output = IdmAktualnosciOtc.scrap()
    print(output)