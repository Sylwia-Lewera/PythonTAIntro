from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#import time
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get('https://scrapingclub.com/exercise/basic_login/')
time.sleep(50)
nameField = driver.find_element_by_xpath('//*[@id="id_name"]')
nameField.send_keys('Name')
#nameField = driver.find_element("xpath",'//*[@id="id_password"]')
#nameField.send_keys('pass')
#loginButton = driver.find_element("xpath",'/html/body/div/div/div[1]/div[3]/form/button')
#time.sleep(5)
#loginButton.click()