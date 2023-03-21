from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from inputinfo import username,password

class Swaglabs:
    def openweb(self):
        self.mybrowser = webdriver.Chrome(ChromeDriverManager().install())
        self.mybrowser.get("https://www.saucedemo.com/")
    
    def logIN(self,username,password):
        user = self.mybrowser.find_element(By.NAME,"user-name")
        passwrd = self.mybrowser.find_element(By.NAME,"password")
        loginButton = self.mybrowser.find_element(By.NAME,"login-button")
        sleep(1)
        if username == "" and password == "":
            user.send_keys(username)
            sleep(0.5)
            passwrd.send_keys(password)
            loginButton.click()
            sleep(3)
            txt=self.mybrowser.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]").text
            print(txt)
            sleep(2)
            self.mybrowser.find_element(By.CLASS_NAME,"error-button").click()
        elif username != "" and password =="":
            user.send_keys(username)
            sleep(1)
            passwrd.send_keys(password)
            loginButton.click()
            sleep(2)
            txt = self.mybrowser.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]").text
            print(txt)
            sleep(2)
            self.mybrowser.find_element(By.CLASS_NAME,"error-button").click()
        elif username == "locked_out_user" and password == "secret_sauce":
            user.send_keys(username)
            sleep(1)
            passwrd.send_keys(password)
            loginButton.click()
            txt = self.mybrowser.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]").text
            print(txt)
            sleep(2)
            self.mybrowser.find_element(By.CLASS_NAME,"error-button").click()
        else:
            user.send_keys(username)
            sleep(1)
            passwrd.send_keys(password)
            sleep(1)
            loginButton.click()
    
    def products(self):
        product = self.mybrowser.find_elements(By.CLASS_NAME,"inventory_item")
        return print(f"{len(product)} adet ürün vardır.")

#username ve password bilgilerini inputinfo.py 'den import ediyoruz.

asd = Swaglabs()
asd.openweb() #web siteyi açıyoruz.
asd.logIN(username, password) #Login işlemimiz.
asd.products()  # ürün sayımızı dönderiyor.