from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	# Открыть ссылку в браузере
	
	button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
	button.click()
	# Кликнуть по кнопке
	
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	# Перейти на новую вкладку
	
	numElement = browser.find_element(By.ID, "input_value")
	num = int(numElement.text)
	result = str(calc(num))
	# Посчитать результат по формуле и перевести его в строку
	
	resField = browser.find_element(By.ID, "answer")
	resField.send_keys(result)
	button2 = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
	button2.click()
	# Вставить результат в поле и нажать на кнопку

finally:
	time.sleep(10)
	browser.quit()
