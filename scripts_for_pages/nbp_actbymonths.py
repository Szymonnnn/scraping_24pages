from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pathlib import Path

class NbpActbymonths:
    def __init__(self) -> None:
        pass

    def scrap():
        end_of_page = 1
        output_string = []
        driver_path =  str(Path(Path.cwd())) + "\edge_webdriver\msedgedriver.exe"
        path_to_file = str(Path(Path.cwd())) + "\last_announcements\last_nbp_actbymonths.txt"
        url = "https://dzu.nbp.pl/actbymonths"
        
        #reading from file last announcement title
        f = open(path_to_file, 'r', encoding='utf-8')
        last_title = f.read()
        f.close()

        driver = webdriver.Edge(executable_path = driver_path)

        driver.get(url)
        try:
            articles = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'act__item-desc')))
            #articles = driver.find_elements_by_class_name("act__item-desc")
            #subjects = articles.find_elements_by_class_name("subject")
            for article in articles:
                title = article.text.strip()

                if title == last_title:
                    end_of_page = 0
                    break

                output_string.append(title)
                link_place = article.find_element_by_class_name("subject")
                link = link_place.get_attribute('href')
                output_string.append(link)

            if end_of_page == 1:
                output_string.append("There are more articles on this page!!!")
                output_string.append("")

            new_title = articles[0].text.strip()
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
    obj = NbpActbymonths()
    output = NbpActbymonths.scrap()
    print(output)