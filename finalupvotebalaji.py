import os

import time
from selenium import webdriver

# phantomjs_path = "C:\\Users\\A572002\\Pictures\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe"

# driver = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
# driver3=webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
chromedriver = "/home/aakash/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
#driver = webdriver.Chrome(chromedriver)
#driver3 = webdriver.Chrome(chromedriver)
driver = webdriver.PhantomJS()
driver3 = webdriver.PhantomJS()
print 'started browser'
driver.get("https://www.quora.com/profile/Balaji-Viswanathan-2")
print 'got to url'
driver.save_screenshot('out4.png');
while True:
    time.sleep(60)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elements = driver.find_elements_by_class_name('answer_permalink')
    print 'size' + str(len(elements))
    w = []
    ans = ""
    for each in elements:

        if len(str(each.get_attribute('href'))) > 6:

            driver3.get(str(each.get_attribute('href')))
            for each in driver3.find_elements_by_css_selector('.AnswerVoterListModalLink.VoterListModalLink'):
                #print str(each.get_attribute('href'))
                each.click()
                time.sleep(10)
                eles=driver3.find_elements_by_class_name('modal_title')
                for each in eles:


                 if int(str(each.text)[:len(str(each.text))-9]) > 6000:
                       print "url  "+driver3.current_url
                       print str(each.text)





