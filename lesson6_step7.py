from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/huge_form.html")
	elements = browser.find_elements(By.TAG_NAME, "input")
	letters = string.ascii_lowercase
	for element in elements:
		random_word = ''.join(random.choice(letters) for _ in range(8))
		element.send_keys(random_word)
		
	button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
	button.click()
	
finally:
	# скопировать код за 30 секунд
	time.sleep(30)
	# закрыть браузер
	browser.quit()
	
#пустая строка на случай запуска на винде
