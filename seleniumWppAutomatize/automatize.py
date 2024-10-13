from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/jlsam/AppData/Local/Google/Chrome/User Data")
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com/")

wait=WebDriverWait(driver,100)
target='"Luis Francisco Faesa"'
message="teste"
number_of_times=5

contact_path='//span[contains(@title,'+ target +')]'
contact=wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
contact.click()
message_box_path='//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]'
message_box=wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
for x in range(number_of_times):
    message_box.send_keys(message + Keys.ENTER)
    time.sleep(0.2)

time.sleep(10)