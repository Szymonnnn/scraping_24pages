from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pathlib import Path

class DziennikUrzedowy:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        driver_path =  str(Path(Path.cwd())) + "\edge_webdriver\msedgedriver.exe"
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_dziennik_urzedowy.txt"
        url = "https://dziennikurzedowy.knf.gov.pl/actbymonths"
        
        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.readline()
        f.close()

        driver = webdriver.Edge(executable_path = driver_path)

        driver.get(url)
        #print(driver.title)
        try:
            articles = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))
            #articles = driver.find_element_by_tag_name("tbody")
            subjects = articles.find_elements_by_class_name("subject")
            for subject in subjects:
                #print("-----------------------------------------------------")
                title = subject.text

                if title == last_title:
                    end_of_page = 0
                    break

                #print(title)
                output_string.append(title)
                link = subject.get_attribute('href')
                #print(link)
                output_string.append(link)
                #print("-----------------------------------------------------")

            if end_of_page == 1:
                output_string.append("There are more articles on this page!!!")
                output_string.append("")

            new_title = subjects[0].text
            driver.quit()
        except:
            driver.quit()
            output_string = []
            output_string.append("There was a problem with reading page!!!")
            output_string.append("")
            return output_string


        f = open(path_to_file, 'w', encoding='utf-8')
        f.write(new_title)
        f.close()
        return output_string

if __name__ == '__main__':
    obj = DziennikUrzedowy()
    output = DziennikUrzedowy.scrap()
    print(output)