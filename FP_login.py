import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://fp.lmu.edu.ng/')

assert 'Landmark University' in driver.title

username_input = driver.find_element(by=By.ID, value='username')
username_input.send_keys('firstname.lastname')

password_input = driver.find_element(by=By.NAME, value='password')
password_input.send_keys('your-silly-password')

login_button = driver.find_element(by=By.CLASS_NAME, value='button')
login_button.click()

# Wait for the login to complete
WebDriverWait(driver, 10).until(EC.title_contains('Landmark University ®'))
nav_item = driver.find_element(By.LINK_TEXT, "Exams & Results")
nav_item.click()
VeiwResult = driver.find_element(by=By.LINK_TEXT, value='View Result')
VeiwResult.click()

from selenium.webdriver.support.ui import Select

# Wait for the "Session" dropdown to be clickable
session_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "session"))
)

# Select "2023/2024" from the "Session" dropdown
select = Select(session_dropdown)
select.select_by_value("131")  # 131 is the value for "2023/2024"

# Wait for the "Semester" dropdown to be clickable
semester_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "semester"))
)

# Select "Alpha" from the "Semester" dropdown
select = Select(semester_dropdown)
select.select_by_value("1")  # 1 is the value for "Alpha"

# Wait for the "Get Result" button to be clickable
get_result_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "get_result"))
)

# Click the "Get Result" button
get_result_button.click()

time.sleep(20)
driver.quit()