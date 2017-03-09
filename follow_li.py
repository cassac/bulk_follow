import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from links import linkedin_urls
from config import li_username, li_password

# Initiate webdriver
driver = webdriver.Chrome()
# Navigate to userpage and login
driver.get("https://www.linkedin.com/")
driver.find_element_by_name('session_key').send_keys(li_username)
driver.find_element_by_name('session_password').send_keys(li_password)
driver.find_element_by_id('login-submit').click()

# Iterate through friends
for url in linkedin_urls:
  linkedin_handle = url.split('/')[-1]

  try:
    driver.get(url)
  except:
    print('ERROR: Invalid URL:' + url)
    continue
  
  try:
    driver.find_element_by_xpath("//*[@id='profile-wrapper']/div[3]/div[1]/section/div[3]/div[2]/button").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//div[@class='modal-wormhole-content']/div/section/div/div[2]/button[2]").click()
    print('SUCCESS: sent invitation to ' + linkedin_handle)
  except:
    try:
      driver.find_element_by_xpath('//span[text()="Accept"]').click()
      print('SUCCESS: accepted invitation from ' + linkedin_handle)
    except:
      print('WARNING: You may already be connected with ' + linkedin_handle)
      
  time.sleep(0.5)

driver.close()
