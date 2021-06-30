from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import time 


username = "" #email address associated with account, used for login and school login
password = getpass("Type in password: ")
Tpassword = getpass("Type in email password: ") # in case two diff passwords for login and school email

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options, executable_path='') # make sure to add path to chromedriver, for selenium


driver.get("https://www.imleagues.com/spa/account/login")

wait = WebDriverWait(driver, 30)

element = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
username_textbox = driver.find_element_by_xpath('//*[@id="email"]')
username_textbox.send_keys(username)
username_textbox.send_keys(u'\ue007')

element = wait.until(EC.element_to_be_clickable((By.ID, 'password')))
password_textbox = driver.find_element_by_xpath('//*[@id="password"]')
password_textbox.send_keys(password)
password_textbox.send_keys(u'\ue007')

wait = WebDriverWait(driver, 30)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="userNameInput"]')))
tUsername = driver.find_element_by_xpath('//*[@id="userNameInput"]')
tUsername.send_keys(username)

element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordInput"]')))
tEmailPass = driver.find_element_by_xpath('//*[@id="passwordInput"]')
tEmailPass.send_keys(Tpassword)
tEmailPass.send_keys(u'\ue007')

driver.get("https://www.imleagues.com/spa/fitness/akTwUN4XHNdgXJmS2YJSBAMM/viewclass?classId=9732")
driver.execute_script("window.scrollTo(0, 2000)")
time.sleep(5)
driver.execute_script("window.scrollTo(0, 2160)")
time.sleep(5)
driver.execute_script("window.scrollTo(0, 3240)")
time.sleep(5)
driver.execute_script("window.scrollTo(0, 5000)")

avail = driver.find_elements(By.CLASS_NAME, "iml-callout-success")
links = []

for b in avail:
	links.append(b.find_element(By.TAG_NAME, 'a'))

openSessionURL = links[-1].get_attribute('href')

driver.get(openSessionURL)

time.sleep(2)
try:
	driver.find_element_by_link_text("Sign Up").click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button').click()
except:
	driver.find_element_by_xpath('//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button').click()

driver.quit()
