import os
import shutil

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def scrape_photos(queries, seconds):

    print('Beginning Scrapping ...')

    photo_path = './photos'
    try:
        shutil.rmtree(photo_path)    
    except: pass
    os.mkdir(photo_path)

    for query in queries:
        ## suppress misc error messages
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver = webdriver.Chrome(options=options,executable_path='./drivers/chromedriver.exe')
        # data = requests.get('https://unsplash.com/s/photos/smile')
        # soup = BeautifulSoup(data.content, 'html.parser')

        url = 'https://unsplash.com/s/photos/' + query
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver.maximize_window()
        driver.get(url)

        # handles the button to show more 
        driver.execute_script("window.scrollTo(0, 400)")
        div = driver.find_element(By.CLASS_NAME, value='gDCZZ')  
        button = div.find_element(By.TAG_NAME, value='button')
        button.click()

        # scrolling thorugh the website
        duration = int(float(seconds) / .2)
        for i in range(duration):
            time.sleep(.2)
            driver.execute_script("window.scrollBy(0, 450)")

        # finding each photo
        images = []
        divs = driver.find_elements(By.CLASS_NAME, value='ripi6')
        for div in divs:
            figures = div.find_elements(By.TAG_NAME, value='figure')
            for figure in figures:
                image = figure.find_element(By.TAG_NAME, value='img')
                images.append(image.get_attribute('src'))

        path = os.path.join(photo_path, query)
        os.mkdir(path)

        # saving each photo
        for i, image in enumerate(images):
            response = requests.get(image)
            new_path = path +'/' + str(i) + '.png'
            file = open(new_path, 'wb')
            file.write(response.content)
            file.close()
        
        print('Query Complete.')
    
    print('Scrapping Completed.')

def even_queries():
    smallest_folder = 100000
    photo_path = './photos'
    for folder in os.listdir(photo_path):
        curr_folder = len(os.listdir(photo_path + '/' + folder))
        if curr_folder < smallest_folder:
            smallest_folder = curr_folder 

    for folder in os.listdir(photo_path):
        curr_folder = os.listdir(photo_path + '/' + folder)
        while len(curr_folder) > smallest_folder:
            os.remove(photo_path + '/' + folder + '/' + curr_folder.pop())
        print(len(curr_folder))


if __name__ == '__main__':

    queries = ['green', 'blue']

    #function to scrape
    scrape_photos(queries, seconds=10)

    # function to even out query results
    even_queries()


    

    
