import os

import time
from selenium import webdriver

chromedriver = "/home/aakash/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.PhantomJS()
driver3= webdriver.PhantomJS()
driver.get("https://www.quora.com/profile/Richard-Muller-3")
#more_link
#driver.execute_script("arguments[0].click();", each)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elements=driver.find_elements_by_class_name('more_link')
    w=[]
    for each in elements:

      if len(str(each.get_attribute('href'))) > 6:
         #print str(each.get_attribute('href'))
         if str(each.get_attribute('href')) not in w:
           w.append(str(each.get_attribute('href')))
           driver3.get(str(each.get_attribute('href')))

           if float(driver3.find_element_by_class_name('meta_num').text[:len(driver3.find_element_by_class_name('meta_num').text)-1]) > 1.0:
               print str(each.get_attribute('href'))
               print driver3.find_element_by_class_name('meta_num').text[:len(driver3.find_element_by_class_name('meta_num').text)-1]

    time.sleep(3)

    #for each in driver.find_elements_by_class_name('pagedlist_item'):
     #  if '?' in each.text:
      #    print each.text
