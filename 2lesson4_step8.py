from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	# Открыть ссылку в браузере
	
	price = WebDriverWait(browser, 12).until(
			EC.text_to_be_present_in_element((By.ID, "price"), "100")
		)
	button = browser.find_element(By.ID, "book")
	button.click()
	
	numElement = browser.find_element(By.ID, "input_value")
	num = int(numElement.text)
	result = str(calc(num))
	# Посчитать результат по формуле и перевести его в строку
	
	resField = browser.find_element(By.ID, "answer")
	resField.send_keys(result)
	button2 = browser.find_element(By.ID, "solve")
	button2.click()
	# Вставить результат в поле и нажать на кнопку
	
finally:
	time.sleep(10)
	browser.quit()
