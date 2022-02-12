import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise")
# driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input[class='search-keyword']").send_keys('ber')


driver.find_element(By.CSS_SELECTOR,"button[class='search-button']").click()
Buttons = driver.find_elements(By.CSS_SELECTOR,"div[class='product-action'] button")
for button in Buttons:
    button.click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))
driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys('rahulshettyacademy')
# driver.find_element(By.CSS_SELECTOR,"button[class='promoBtn']").click()
driver.find_element(By.XPATH,"//button[text()='Apply']").click()

couponmessage = driver.find_element(By.XPATH,"//span[text()='Code applied ..!']").text
assert couponmessage in 'Code applied ..!'

