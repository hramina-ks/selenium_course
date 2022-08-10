from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import random
import string

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)
	# Открыть ссылку в браузере
	
	letters = string.ascii_lowercase
	# Переменная для алфавита
	
	firstname = browser.find_element(By.NAME, "firstname")
	random_name = ''.join(random.choice(letters) for _ in range(7))
	firstname.send_keys(random_name)
	
	lastname = browser.find_element(By.NAME, "lastname")
	random_name = ''.join(random.choice(letters) for _ in range(7))
	lastname.send_keys(random_name)
	
	email = browser.find_element(By.NAME, "email")
	email.send_keys("test@test.com")
	
	attach = browser.find_element(By.ID, "file")
	current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, "test.txt")
	attach.send_keys(file_path) #добавляем путь в поле для файла
	
	btn = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
	btn.click()
	
finally:
	time.sleep(10)
	browser.quit()
