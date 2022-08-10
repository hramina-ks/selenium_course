from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
import unittest 

class TestRegist(unittest.TestCase):
	def test_reg1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		# Открываем браузер
		
		letters = string.ascii_lowercase
		# Переменная для алфавита
		
		firstname = browser.find_element(By.CLASS_NAME, "first")
		random_name = ''.join(random.choice(letters) for _ in range(8))
		firstname.send_keys(random_name)
		# Заполняем рандомом поле firstname
		
		lastname = browser.find_element(By.CLASS_NAME, "second")
		random_lastname = ''.join(random.choice(letters) for _ in range(10))
		lastname.send_keys(random_lastname)
		# Заполняем рандомом поле lastname
		
		email = browser.find_element(By.CLASS_NAME, "third")
		email.send_keys("test@test.com")
		# Заполняем поле email
		
		button = browser.find_element(By.TAG_NAME, "button")
		button.click()
		# Отправляем форму
		
		time.sleep(1)
		# Ждем загрузки страницы
		
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		# Находим на странице заголовок
		
		welcome_text = welcome_text_elt.text
		# Получаем текст заголовка
		
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "No welcome text")
		#assert "Congratulations! You have successfully registered!" == welcome_text
		# Убеждаемся, что попали на нужную страницу
		
	def test_reg2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		# Открываем браузер
		
		letters = string.ascii_lowercase
		# Переменная для алфавита
		
		firstname = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
		random_name = ''.join(random.choice(letters) for _ in range(8))
		firstname.send_keys(random_name)
		# Заполняем рандомом поле firstname
		
		lastname = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
		random_lastname = ''.join(random.choice(letters) for _ in range(10))
		lastname.send_keys(random_lastname)
		# Заполняем рандомом поле lastname
		
		email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
		email.send_keys("test@test.com")
		# Заполняем поле email
		
		button = browser.find_element(By.TAG_NAME, "button")
		button.click()
		# Отправляем форму
		
		time.sleep(1)
		# Ждем загрузки страницы
		
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		# Находим на странице заголовок
		
		welcome_text = welcome_text_elt.text
		# Получаем текст заголовка
		
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "No welcome text")
		#assert "Congratulations! You have successfully registered!" == welcome_text
		# Убеждаемся, что попали на нужную страницу
		

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
