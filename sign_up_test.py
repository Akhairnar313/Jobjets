from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
#open website
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
#click on sign in button
register_button = driver.find_element(By.ID,"pages")
register_button.click()
time.sleep(5);
employer_register_button = driver.find_element(By.ID,"employersss")
employer_register_button.click()
time.sleep(5);
print("-register modal opened")
driver.find_element(By.NAME,'first_name').send_keys('Test_Employer')
driver.find_element(By.NAME,'last_name').send_keys('Test_Address')
driver.find_element(By.NAME,'email').send_keys('test_email@gmail.com')
driver.find_element(By.NAME,'password1').send_keys('12345')
driver.find_element(By.NAME,'password2').send_keys('12345')
print("-Registration form filled")
time.sleep(5);
ActionChains(driver).move_to_element(driver.find_element(By.ID,"register_button")).click().perform()
time.sleep(5);



print(" \n\n\n___ Test Success ____\n\n\n")

time.sleep(10)

driver.quit()
