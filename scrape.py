import os
import shutil

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


if __name__ == '__main__':
    
    emotions = ['smiling', 'angry']

    for emotion in emotions:

        ## suppress misc error messages
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver = webdriver.Chrome(options=options,executable_path='./drivers/chromedriver.exe')

        # data = requests.get('https://unsplash.com/s/photos/smile')
        # soup = BeautifulSoup(data.content, 'html.parser')
        url = 'https://unsplash.com/s/photos/' + emotion
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver.maximize_window()
        driver.get(url)

        # handles the button to show more 
        driver.execute_script("window.scrollTo(0, 400)")
        div = driver.find_element(By.CLASS_NAME, value='gDCZZ')  
        button = div.find_element(By.TAG_NAME, value='button')
        button.click()

        # scrolling thorugh images
        for i in range(10):
            time.sleep(.2)
            driver.execute_script("window.scrollBy(0, 450)")
        
        images = []
        divs = driver.find_elements(By.CLASS_NAME, value='ripi6')
        for div in divs:
            figures = div.find_elements(By.TAG_NAME, value='figure')
            print(len(figures))
            for figure in figures:
                image = figure.find_element(By.TAG_NAME, value='img')
                images.append(image.get_attribute('src'))


        # if directory already exists
        path = os.path.join('./', emotion)
        try:
            shutil.rmtree(path)    
        except: pass

        os.mkdir(path)

        # saving each image
        for index, image in enumerate(images):
            response = requests.get(image)
            path = './'+ emotion +'/' + str(index) + '.png'
            file = open(path, 'wb')
            file.write(response.content)
            file.close()
