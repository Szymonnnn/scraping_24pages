from bs4 import BeautifulSoup
import requests
from pathlib import Path

class UknfSektorBaknowy:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_uknf_sektor_bankowy.txt"
        url = "https://www.knf.gov.pl/dla_rynku/stanowiska/stanowiska_uknf_sektor_bankowy"

        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.read()
        f.close()

        #reading html from web site
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")

        announcements = doc.find("div", {"class": "main-content"})
        #print(announcements.prettify())
        ogloszenia = announcements.find_all("li")
        for ogloszenie in ogloszenia:
            title = ogloszenie.text
            if title == last_title:
                end_of_page = 0
                break
            #print(title)
            #print(last_title)
            #print("------------------------------------------------------")
            output_string.append(title)
            try:
                hrief = ogloszenie.find("a", href=True)
                link = hrief['href']
                if link[0:22] != "https://www.knf.gov.pl":
                    link = "https://www.knf.gov.pl" + link
                output_string.append(link)
                #print(link)
                #print("-------------------------------------------------------------------------\n")
            except:
                output_string.append("")
                #print("############################SKIPED##########################")

        if end_of_page == 1:
            output_string.append("There are more articles on this page!!!")
            output_string.append("")

        new_title = ogloszenia[0].text
        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = UknfSektorBaknowy()
    output = UknfSektorBaknowy.scrap()
    print(output)