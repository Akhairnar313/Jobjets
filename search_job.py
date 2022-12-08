from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

#open website
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")

#Registering Employer
register_button = driver.find_element(By.ID,"pages")
register_button.click()
time.sleep(0.25);
employer_register_button = driver.find_element(By.ID,"employersss")
employer_register_button.click()
time.sleep(0.25);
print("-register modal opened")
driver.find_element(By.NAME,'first_name').send_keys('Test_Employer')
driver.find_element(By.NAME,'last_name').send_keys('Test_Address')
driver.find_element(By.NAME,'email').send_keys('test_email@gmail.com')
driver.find_element(By.NAME,'password1').send_keys('12345')
driver.find_element(By.NAME,'password2').send_keys('12345')
print("-Registration form filled")
time.sleep(0.25);
ActionChains(driver).move_to_element(driver.find_element(By.ID,"register_button")).click().perform()
time.sleep(0.25);

# Logging in as recently registered employer
sign_in_button = driver.find_element(By.ID,"login")
sign_in_button.click()
print("-login modal opened")
driver.find_element(By.NAME,'email').send_keys('test_email@gmail.com')
driver.find_element(By.NAME,'password').send_keys('12345')
print("-Log in form filled")
time.sleep(0.25);
driver.find_element(By.XPATH,"//*[contains(text(), 'Log in')]").click()

# Using the Search job funcionality
driver.find_element(By.NAME,'position').send_keys('Android Developer')
driver.find_element(By.NAME,'location').send_keys('Pune')
time.sleep(0.25)
ActionChains(driver).move_to_element(driver.find_element(By.ID,"search_button")).click().perform()
time.sleep(0.25)

# Creating a new position
ActionChains(driver).move_to_element(driver.find_element(By.ID,"clientZone")).click().perform()
time.sleep(0.25)
ActionChains(driver).move_to_element(driver.find_element(By.ID,"create_job")).click().perform()
time.sleep(0.25)
driver.find_element(By.NAME,'title').send_keys('test job title')
driver.switch_to.frame("description_ifr")
driver.find_element(By.ID,'tinymce').send_keys('test description of job')
driver.switch_to.parent_frame()
driver.find_element(By.ID,'salary').send_keys('50000')
driver.find_element(By.CLASS_NAME,'select2-search__field').click()
time.sleep(.25)
driver.find_element(By.XPATH,"//*[contains(text(), 'PHP')]").click()
driver.find_element(By.ID,'location').send_keys('Banglore,Karnataka')
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//*[@title='Full time']")).click().perform()
driver.find_element(By.ID,'apply_url').send_keys('https://in.linkedin.com/')
driver.find_element(By.ID,'validity').send_keys('01-01-2023')
driver.find_element(By.ID,'company_name').send_keys('Test_Employer')
driver.switch_to.frame("company_description_ifr")
driver.find_element(By.ID,'tinymce').send_keys('test description for company')
driver.switch_to.parent_frame()
driver.find_element(By.ID,'company_website').send_keys('https://in.indeed.com/')
ActionChains(driver).move_to_element(driver.find_element(By.ID,'save_publish')).click().perform()
time.sleep(2)
print("-Create new Job form filled")

# Logging out(Employer)
ActionChains(driver).move_to_element(driver.find_element(By.ID,"clientZone")).click().perform()
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//*[contains(text(), 'Logout')]")).click().perform()
time.sleep(5)

# Logging in as an employee
driver.find_element(By.NAME,'email').send_keys('yash@gmail.com')
driver.find_element(By.NAME,'password').send_keys('12345')
print("-Log in form filled")
time.sleep(0.25);

#Searching for the recently created postion
driver.find_element(By.XPATH,"//*[contains(text(), 'Log in')]").click()
driver.find_element(By.NAME,'position').send_keys('test job title')
driver.find_element(By.NAME,'location').send_keys('Banglore,Karnataka')
time.sleep(0.25)
ActionChains(driver).move_to_element(driver.find_element(By.ID,"search_button")).click().perform()
time.sleep(0.25)

# Applying for the position
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//*[contains(text(), 'test job title')]")).click().perform()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
ActionChains(driver).move_to_element(driver.find_element(By.ID,"apply-job")).click().perform()
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//*[contains(text(), 'Applications')]")).click().perform()

# Logging out (Employee)
ActionChains(driver).move_to_element(driver.find_element(By.ID,"clientZone")).click().perform()
time.sleep(0.25)
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//*[contains(text(), 'Logout')]")).click().perform()

# Logging in(Employer)
driver.find_element(By.NAME,'email').send_keys('test_email@gmail.com')
driver.find_element(By.NAME,'password').send_keys('12345')
print("-Log in form filled")
time.sleep(0.25);
driver.find_element(By.XPATH,"//*[contains(text(), 'Log in')]").click()

#Displaying all the applicants
ActionChains(driver).move_to_element(driver.find_element(By.ID,"clientZone")).click().perform()
time.sleep(0.25)
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//*[contains(text(), 'Applicants')]")).click().perform()

# Sending response to an employee
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//*[contains(text(), 'Yash Jadhav')]")).click().perform()
ActionChains(driver).move_to_element(driver.find_element(By.ID,"send-response")).click().perform()
time.sleep(2)
driver.find_element(By.ID,'comment_section').send_keys('Well Done !!!')
driver.find_element(By.XPATH,"//*[@value='Send']").click()

# Logging out (Employer)
ActionChains(driver).move_to_element(driver.find_element(By.ID,"clientZone")).click().perform()
time.sleep(0.25)
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//*[contains(text(), 'Logout')]")).click().perform()

# Logging in (Employee)
driver.find_element(By.NAME,'email').send_keys('yash@gmail.com')
driver.find_element(By.NAME,'password').send_keys('12345')
print("-Log in form filled")
time.sleep(0.25);
driver.find_element(By.XPATH,"//*[contains(text(), 'Log in')]").click()

# Checking status for the position
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//*[contains(text(), 'Applications')]")).click().perform()
time.sleep(5)

print(" \n\n\n___ Test Success ____\n\n\n")
time.sleep(10)
driver.quit()