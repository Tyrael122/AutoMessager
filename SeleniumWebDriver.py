from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://web.whatsapp.com/")

contacts = [":l"]
for contact in contacts:
    while True:
        try:
            browser.find_element(By.XPATH, f"//span[@title='{contact}']").click()
        except:
            continue
        break
    messageBar = browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    messageBar.send_keys(f"Oi {contact}, estou usando Python pra mandar essa mensagem pra você", Keys.ENTER)

print("Opened successfully")



