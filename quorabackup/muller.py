import os

import time
from selenium import webdriver


driver = webdriver.PhantomJS()
driver.get("https://www.quora.com/Do-Indians-realize-what-they-have-done-to-Quora/answer/Deepak-Mehta-2")
ele=driver.find_elements_by_class_name('qtext_para')
for each in ele:
  print str(each)
