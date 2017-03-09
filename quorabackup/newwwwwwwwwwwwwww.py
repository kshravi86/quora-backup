import os

import time
from selenium import webdriver


phantomjs_path = "C:\\Users\\A572002\\Pictures\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe"

driver = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
driver3=webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
#driver = webdriver.PhantomJS()
#driver3 = webdriver.PhantomJS()
print 'started browser'
driver.get("https://www.quora.com/profile/Deepak-Mehta-2")
print 'got to url'
driver.save_screenshot('out3.png');
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elements = driver.find_elements_by_class_name('answer_permalink')
    print 'size' + str(len(elements))
    w = []
    for each in elements:
        #print each.text
        if len(str(each.get_attribute('href'))) > 6:
            #print str(each.get_attribute('href'))
            driver3.get(str(each.get_attribute('href')))
            if float(driver3.find_element_by_class_name('meta_num').text[:len(driver3.find_element_by_class_name('meta_num').text) - 1]) > 100.0:
               print str(each.get_attribute('href'))
               print driver3.find_element_by_class_name('meta_num').text[
                  :len(driver3.find_element_by_class_name('meta_num').text) - 1]

    time.sleep(3)
