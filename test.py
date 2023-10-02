from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get("google.com")