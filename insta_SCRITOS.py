user = input("digite seu uname do insta--:")
from playwright.sync_api import sync_playwright
import time   
with sync_playwright() as p:
 navegador = p.firefox.launch()
 pagina = navegador.new_page()
 pagina.goto("https://www.instagram.com")
 time.sleep(5)
 #email
 pagina.fill('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input',"yagabe8271")
 time.sleep(5)
 #senha
 pagina.fill('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input',"12131415")
 time.sleep(5)
 #button clic
 pagina.locator('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()
 time.sleep(10)
 pagina.goto(f"https://www.instagram.com/{user}/")
 #pagina.locator('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[2]').click()
 #time.sleep(5)
 #pagina.fill('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input',user)
 #time.sleep(5)
 #pagina.locator('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a/div[1]/div/div/div[2]/div/div/div/span').click()
 #time.sleep(5)
 #button folow
 pagina.locator('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div/button/div/div').click()
 #isso ai
 time.sleep(10)
 
 print("obrigado por ultilizar nossos services voce tem 1 seguidor")
 bot = input("tecle enter para finalizar ...")
 print(bot)
 time.sleep(5)