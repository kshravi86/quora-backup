import os

import time
from selenium import webdriver


driver = webdriver.PhantomJS()
  
  
 
 
driver.get("https://www.quora.com/Why-did-Apple-remove-the-escape-key-from-the-new-Macbook/answer/Deepak-Mehta-2")
ele=driver.find_elements_by_class_name('qtext_para')
ans="<html><body>"
for each in ele:
   print each.text
   
   yourstring=each.text
   yourstring = yourstring.encode('ascii', 'ignore').decode('ascii')
   ans=ans+'<br>'+yourstring
   
ans=ans+"</body></html>"
f=open('subbu.txt','w')
f.write(ans)
   


 
 
 
  
 
 
 
 
 
 



