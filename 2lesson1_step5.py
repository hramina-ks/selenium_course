from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)
	# Открыть ссылку в браузере
	
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)
	field = browser.find_element(By.ID, "answer")
	field.send_keys(y)
	# Посчитать значение и заполнить поле
	
	checker = browser.find_element(By.ID, "robotCheckbox")
	checker.click()
	# Найти и отметить чекбокс
	
	radiobut = browser.find_element(By.ID, "robotsRule")
	radiobut.click()
	# Найти и отметить радиобаттон
	
	but = browser.find_element(By.CSS_SELECTOR, ".btn-default")
	but.click()
	
finally:
	time.sleep(10)
	browser.quit()
	
