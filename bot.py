from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.pokemon.com/br/pokedex/")

login = driver.find_element(By.TAG_NAME, "li")
login.click()

# Form
#email = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.ID, "username"))
#)
#password = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.ID, "password"))
#)

# Sending info
#email.send_keys("develoopersenior@gmail.com")
#password.send_keys("12345X4321")

#password.submit()

#WebDriverWait(driver, 10).until(EC.url_contains("linkedin.com/feed/"))

# Pesquisando Python
#search = driver.find_element(By.ID, "global-nav-search")
#search.send_keys("Python")
#search.submit()

input('')

#pesquisar.click()
#search_input.send_keys("Python")
#search_input.submit()

#WebDriverWait(browser, 10).until(EC.url_contains("linkedin.com/search/results"))

# Filtro Vagas
#vagas_filter = driver.find_element_by_xpath("//button[contains(text(), 'Vagas')]")
#vagas_filter.click()