import time
import sys
from splinter import Browser                
with Browser() as browser: 

 

  browser.visit('https://mymasonportal.gmu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_66_1')
  browser.fill('user_id', 'bbehmard')
  browser.fill('password', 'Arshia.1985!')
  browser.find_by_id('entry-login').first.click()
  browser.click_link_by_partial_href('/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_230_1')


#  sleep(9000)  
  while 1:
    	time.sleep(5)
  try:
       	b = browser.find_by_tag("body")      
  except:
      	sys.exit()


#copied_text = browser.find_by_id('login')[0].text
