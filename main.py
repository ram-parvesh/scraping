from selenium import webdriver
from save_images import make_directory, save_images, save_data_to_csv
from scrap_image import scrap_image_url
from selenium.common.exceptions import StaleElementReferenceException
import os
# Creating an instance of google chrome
DRIVER_PATH = os.path.join(os.getcwd(),"chromedriver")

# TO run Chrome in a headfull mode(li.ke regular chrome)
driver = webdriver.Chrome (executable_path= DRIVER_PATH)
current_page_url = driver.get('https://www.flipkart.com/clothing-and-accessories/topwear/shirt/men-shirt/formal-shirt/pr?sid=clo,ash,axc,mmk,bk1&otracker=categorytree&otracker=nmenu_sub_Men_0_Formal%20Shirts')

DIRNAME = "men_shrts"
make_directory(DIRNAME)
start_page = 1
total_pages = 5
# Scraping the pages

for page in range(start_page, total_pages+1):
    try :
        product_details = scrap_image_url(driver=driver)
        print('scraping Page {0} of {1} pages'.format(page, total_pages))
        print(product_details)

        page_value = driver.find_element_by_xpath("//a[@class='ge-49M _2Kfbh8']").text
        print('The current page scraped is {}'.format(page_value))

        # Downloads.ng the images
        save_images(data=product_details, dirname= DIRNAME, page=page)
        print('scraping of pages {0} done'.format(page))

        # Saving the data into a csv file
        #save_data_to_csv(data=product_details, filename= 'men_shrts.csv')

        # Moving to the next page
        print('Moving the the next page')
        button_type= driver.find_element_by_xpath ("//div[@class='_2MImiq']//a[@class='_1LKTO3']//span").get_attribute('innerHTML')

        if button_type == 'Next':
            driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
        else:
            driver.find_element_by_xpath("//a[@class='_1LKTO3'][2]").click()

        new_page= driver.find_element_by_xpath("//a[@class='ge-49M _2Kfbh8']").text
        print('The new page is {}'.format(new_page))

    except StaleElementReferenceException as exception:
        print('we are facing an exception')

        exc_page= driver.find_element_by_xpath("//a[@class='ge-49M _2Kfbh8']").text
        print('the page value at the time of exception is {}'.format(exc_page))

        value= driver.find_element_by_xpath("//a[@class='ge-49M _2Kfbh8']")
        link= value.get_attribute('href')
        driver.get(link)

        product_details = scrap_image_url(driver=driver)
        print('scraping Page {0} of {1} pages'.format(page, total_pages))

        page_value = driver.find_element_by_xpath("//a[@class='ge-49M _2Kfbh8']").text
        print('The current page scraped is {}'.format(page_value))

        # Downloads.ng the images
        save_images(data=product_details, dirname=DIRNAME, page=page)
        print('scraping of pages {0} done'.format(page))

        # Saving the data into a csv file
        #save_data_to_csv(data=product_details, filename='men_cloths.csv')

        # Moving to the next page
        print('Moving the the next page')
        button_type = driver.find_element_by_xpath("//div[@class='_2MImiq']//a[@class='_1LKTO3']//span").get_attribute('innerHTML')

        if button_type == 'Next':
            driver.find_element_by_xpath("//a[@class='_1LKTO3']").click()
        else:
            driver.find_element_by_xpath("//a[@class='_1LKTO3'][2]").click()

        new_page= driver.find_element_by_xpath("//a[@class='ge-49M _2Kfbh8']").text
        print('The new page is {}'.format(new_page))






