from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

#ChromeDriverManager().install() kırom driverını otomatik indirip kullanıma imkan sağlar
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.maximize_window() #tam ekran
driver.get("https://www.google.com/") #açılacak url
inp = driver.find_element(By.NAME,"q") #name attributesi q olan elementi çektik
inp.send_keys("kodlamaio") #aramaya kodlamaio yazdırdık
searchButton = driver.find_element(By.NAME,"btnK")
sleep(1)
searchButton.click()

while True:
    continue