import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.find_element(By.CSS_SELECTOR,"input[name= 'name']").send_keys("input ")
# driver.find_element(By.XPATH,"//input[@name= 'name']").send_keys("by xpath ")
#
# driver.find_element(By.CSS_SELECTOR,"input[id= 'exampleCheck1']").click()
#
# driver.find_element(By.CSS_SELECTOR,"input[id='inlineRadio1']").click()
#
#
# dropdown = Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
# dropdown.select_by_index(0)
# # dropdown.select_by_value("Female")
# time.sleep(5)
# dropdown.select_by_visible_text('Female')
# time.sleep(5)
# dropdown.select_by_index(1)
#
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# successmessage=driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text
# print(successmessage)
# try:
#     assert 'Success! The Form has been submitted successfully!.' in successmessage
#     print("successfull message populated")
# except:
#     print("successfull message not populated")


# driver=webdriver.Chrome(executable_path='C:\\chromedriver.exe')
# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.find_element(By.CSS_SELECTOR,"input[id='autosuggest']").send_keys('Ind')
# time.sleep(5)
# listitems=driver.find_elements(By.CSS_SELECTOR,"a[class='ui-corner-all']")
# print(listitems)
#
# for country in listitems:
#     if country.text=='India':
#         country.click()
#         break
# selection= driver.find_element(By.CSS_SELECTOR,"input[id='autosuggest']").get_attribute('value')
# try:
#     assert selection == "India"
#     print("succesfull")
# except:
#     print("unsuccesfull")



driver=webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
listButtons=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(listButtons)

for eachcheckbox in listButtons:
    if eachcheckbox.get_attribute('value') == 'option2':
        eachcheckbox.click()