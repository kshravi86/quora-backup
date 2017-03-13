import os

import time
from selenium import webdriver

#chromedriver = "/home/aakash/Downloads/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
#driver = webdriver.PhantomJS()
phantomjs_path = "C:\\Users\\A572002\\Pictures\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe"

driver = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
#driver3=webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
w=[]
w.append('https://www.quora.com/How-do-astronauts-dry-their-washed-clothes-in-space/answer/Robert-Frost-1')
w.append('https://www.quora.com/What-kinds-of-pens-work-in-space/answer/Robert-Frost-1')
w.append('https://www.quora.com/Does-the-Queen-of-England-actually-do-anything/answer/Robert-Frost-1')
w.append('https://www.quora.com/Does-Robert-Frost-know-who-is-following-him-anymore/answer/Robert-Frost-1')
w.append('https://www.quora.com/If-Indians-can-work-for-NASA-why-cant-they-work-for-SpaceX/answer/Robert-Frost-1')
w.append('https://www.quora.com/Why-do-US-school-grades-go-A-B-C-D-and-F-Why-not-E/answer/Robert-Frost-1')
w.append('https://www.quora.com/Who-cleans-up-all-the-messes-made-by-the-superheroes-in-movies-and-TV-shows/answer/Robert-Frost-1')
w.append('https://www.quora.com/Why-does-the-brain-not-start-recording-memory-for-the-first-few-years-of-life/answer/Robert-Frost-1')
w.append('https://www.quora.com/How-does-the-Hubble-Telescope-avoid-hitting-space-debris/answer/Robert-Frost-1')
w.append('https://www.quora.com/Why-did-Buzz-Aldrin-let-Neil-Armstrong-get-off-the-lunar-module-first-and-take-all-the-credit-for-being-the-first-human-on-the-moon/answer/Robert-Frost-1')
w.append('https://www.quora.com/Does-time-exist-in-space/answer/Robert-Frost-1')
w.append('https://www.quora.com/Is-it-true-that-a-person-who-is-in-space-will-age-slower-than-he-would-have-on-Earth-Why/answer/Robert-Frost-1')
for each in w:
    #print "\""+each[22:len(each)-22]+"?"+"\","
    driver.get(each)
    print driver.find_element_by_class_name('rendered_qtext').text
    time.sleep(3)
    print '<html><body>'
    for each in driver.find_elements_by_class_name('qtext_para'):
     print '<br>'+each.text
    print '</body></html>'
