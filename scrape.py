import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


if __name__ == '__main__':
    print('Hello World!')

    # data = requests.get('https://unsplash.com/s/photos/smile')
    # soup = BeautifulSoup(data.content, 'html.parser')
    url = 'https://unsplash.com/s/photos/smile'
    driver = webdriver.Chrome('./drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get(url)
    

    # handles the button to show more 
    driver.execute_script("window.scrollTo(0, 400)")
    div = driver.find_element(By.CLASS_NAME, value='gDCZZ')  
    button = div.find_element(By.TAG_NAME, value='button')
    button.click()

    for i in range(30):
        time.sleep(.2)
        driver.execute_script("window.scrollBy(0, 450)")

    image_tags = driver.find_elements(By.CLASS_NAME, value='YVj9w')
    images = []
    for image in image_tags:
        images.append(image.get_attribute('src'))

    print(images)
    print(len(images))
    
