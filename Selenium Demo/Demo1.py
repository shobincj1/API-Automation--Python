import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# print(driver.title)

# driver.find_element(By.NAME,"name").send_keys("nobin")
# # driver.find_element(By.CLASS_NAME,"form-control ng-pristine ng-invalid ng-touched").send_keys("class name")
# driver.find_element(By.ID,"exampleCheck1").click()

# driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys('test@test.com')
# driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys('pass')
# driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
# success = driver.find_element(By.CLASS_NAME,"alert-success").text
# print(success)
# try:
#     assert 'Success! The Form has been submitted successfully!.' in success
#     print("success message is validated")
# except:
#     print('success assertion has failed')
#
#
#
#
# dropdown = Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
# dropdown.select_by_index(1)
# dropdown.select_by_index(0)

#
# driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.get("https://login.salesforce.com/")
# print(driver.find_element(By.CSS_SELECTOR,"label[class*='usernamelabel']").text)
# print(driver.find_element(By.XPATH,"//label[@for='username']").text)
#
# print(driver.find_element(By.XPATH,"//form[@id='login_form']/div[1]").text)
# print(driver.find_element(By.CSS_SELECTOR,"form[id='login_form'] label[for='password']").text)
# print(driver.find_element(By.CSS_SELECTOR,"form[id='login_form'] div[id='usernamegroup'] label[for='username']").text)
#
# print(driver.find_element(By.LINK_TEXT,'Forgot Your Password?').text)
#
# driver.find_element(By.LINK_TEXT,'Forgot Your Password?').click()



driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# time.sleep(25)
driver.find_element(By.CSS_SELECTOR,"input[id='autosuggest']").send_keys("ind")
time.sleep(5)
country = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(country))
for cntr in country:
    print(cntr)
    print(cntr.text)
    if cntr.text=="India":
       cntr.click()
       break

print(driver.find_element(By.CSS_SELECTOR,"input[id='autosuggest']").get_attribute('value'))


driver=webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
listButtons=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(listButtons)

for eachcheckbox in listButtons:
    if eachcheckbox.get_attribute('value') == 'option2':
        eachcheckbox.click()