from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from time import sleep

options = Options()
options.headless = False

# Abrindo o sistema
driver = webdriver.Chrome(options=options)
link_system = "http://localhost:8080/"
driver.get(url=link_system)

sleep(1)

#12:10 https://www.youtube.com/watch?v=0xiiTqPkcc8&ab_channel=AndersonFabianoDums