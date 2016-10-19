import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from links import github_urls
from config import username, password

# Initiate webdriver
driver = webdriver.Chrome()
# Navigate to userpage and login
driver.get("https://github.com/" + username)
driver.find_element_by_link_text('Sign in').click()
driver.find_element_by_name('login').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_name('commit').click()

# Iterate through friends
for url in github_urls[34:]:
  github_handle = url.split('/')[-1]
  try:
    driver.get(url)
    time.sleep(1)
    driver.find_elements_by_xpath("//button[@aria-label='Follow this person']")[1].click()
    print 'SUCCESS: added ' + github_handle + "'s Github"
  except:
    print 'ERROR: ' + github_handle + "'s Github handle may be incorrect."
  time.sleep(1)

driver.close()
